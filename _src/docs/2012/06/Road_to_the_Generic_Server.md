这是整本书中最重要的一节，所以读一遍、读两遍、读一百遍——直到你懂透所有。

我们将写四个小的server，分别叫server1，server2。。。，每个和前一个稍有不同。我们的目标是将问题的非功能部分和功能部分彻底分开。上句话对你来说可能不是十分明了，但不用担心，很快就会明白。深吸一口气。。。

Server 1: The Basic Server
----------------------

这是我们第一个尝试。它是一个很小的可以给他一个回调module当做参数的server。

server1.erl

    :::erlang
    -module(server1).
    -export([start/2, rpc/2]).

    start(Name, Mod) ->
        register(Name, spawn(fun() -> loop(Name, Mod, Mod:init()) end)).

    rpc(Name, Request) ->
        Name ! {self(), Request},
        receive
            {Name, Response} -> Response
        end.

    loop(Name, Mod, State) ->
        receive
            {From, Request} ->
                {Response, State1} = Mod:handle(Request, State),
                From ! {Name, Response},
                loop(Name, Mod, State1)
        end.


这一小段代码表现了一个server的最典型最精华的部分，表现了一个server的本质。下面让我们给server写一个回调module。下面是一个名字server回调：

    :::erlang
    -module(name_server).
    -export([init/0, add/2, whereis/1, handle/2]).
    -import(server1, [rpc/2]).

    %% client routines
    add(Name, Place) -> rpc(name_server, {add, Name, Place}).
    whereis(Name) -> rpc(name_server, {whereis, Name}).

    %% callback routines
    init() -> dict:new().

    handle({add, Name, Place}, Dict) -> {ok, dict:store(Name, Place, Dict)};
    handle({whereis, Name}, Dict) -> {dict:find(Name, Dict), Dict}.


这段代码完成了两个任务。一、它是上面的server框架的一个回调module；二、它包含一些可以被客户端调用的接口。`OTP`的惯例就是将上面两个方面放在同一个module中。

可以通过下面代码来证明上述代码可行：

    :::erl
    1> server1:start(name_server, name_server).
    true
    2> name_server:add(joe, "at home").
    ok
    3> name_server:whereis(joe).
    {ok,"at home"}

停下来思考一下。这个回调没有任何并行（concurrency）代码，没有spawn，没有send，没有receive，没有register。它仅仅是纯顺序（sequential）代码而已。这代表什么意思呢？

这代表我们可以在完全不懂并行模型的情况下写出CS（client-server）模型。

这就是所有server的基本模式。一旦你理解了这个基本结构，你便上路了。

Server 2: A Server with Transactions
---------------------

这是一个server，但请求产生异常时，它会将client退掉（crash）。

server2.erl

    :::erlang
    -module(server2).
    -export([start/2, rpc/2]).

    start(Name, Mod) ->
        register(Name, spawn(fun() -> loop(Name, Mod, Mod:init()) end)).

    rpc(Name, Request) ->
        Name ! {self(), Request},
        receive
            {Name, crash} -> exit(rpc);
            {Name, ok, Response} -> Response
        end.

    loop(Name, Mod, OldState) ->
        receive
            {From, Request} ->
                try Mod:handle(Request, OldState) of
                    {Response, State1} ->
                        From ! {Name, ok, Response},
                        loop(Name, Mod, State1)
                catch
                    _:Why ->
                        log_the_error(Name, Request, Why),
                        %% send a message to cause the client to crash
                        From ! {Name, crash},
                        %% loop with the *original* state
                        loop(Name, Mod, OldState)
                end
        end.

    log_the_error(Name, Request, Why) ->
        io:format("Server ~p request ~p ~n"
                  "caused exception ~p~n",
                  [Name, Request, Why]).



这个server增加了事务处理语义（transaction semantics）。

注意这个回调module和之前给server1用的一模一样。只修改server，不动回调module，我们就可以修改回调module的非功能行为。

Server 3: A Server with Hot Code Swapping
-------------------------

现在我们将实现代码热更新：

server3.erl

    :::erlang
    -module(server3).
    -export([start/2, rpc/2, swap_code/2]).

    start(Name, Mod) ->
        register(Name, spawn(fun() -> loop(Name, Mod, Mod:init()) end)).

    swap_code(Name, NewMode) -> rpc(Name, {swap_code, NewMode}).

    rpc(Name, Request) ->
        Name ! {self(), Request},
        receive
            {Name, Response} -> Response
        end.

    loop(Name, Mod, OldState) ->
        receive
            {From, {swap_code, NewCallBackMod}} ->
                From ! {Name, ack},
                loop(Name, NewCallBackMod, OldState);
            {From, Request} ->
                {Response, NewState} = Mod:handle(Request, OldState),
                From ! {Name, Response},
                loop(Name, Mod, NewState)
        end.


它是如何工作的呢？

如果我们发送 swap code 消息，它就会将回调module更新为消息所包含的module。我们先继续用name_server来实验：

    :::erl
    1> server3:start(name_server, name_server1).
    true
    2> name_server:add(joe, "at home").
    ok
    3> name_server:add(helen, "at work").
    ok



假设我们想列出server的所有名字。而当前name_server没有此API。没问题！我们以闪电的速度打开文本编辑器，写一个新的回调模块。

new_name_server.erl

    :::erlang
    -module(new_name_server).
    -export([init/0, add/2, all_name/0, delete/1, whereis/1, handle/2]).
    -import(server3, [rpc/2]).

    %% interface
    add(Name, Place) -> rpc(name_server, {add, Name, Place}).
    all_name() -> rpc(name_server, allNames).
    delete(Name) -> rpc(name_server, {delete, Name}).
    whereis(Name) -> rpc(name_server, {whereis, Name}).

    %% callback routines
    init() -> dict:new().

    handle({add, Name, Place}, Dict) -> {ok, dict:store(Name, Place, Dict)};
    handle(allNames, Dict) -> {dict:fetch_keys(Dict), Dict};
    handle({delete, Name}, Dict) -> {ok, dict:erase(Name, Dict)};
    handle({whereis, Name}, Dict) -> {dict:find(Name, Dict), Dict}.


我们编译它并告诉server将回调更新到这个新module上：

    :::erl
    4> c(new_name_server).
    {ok,new_name_server}
    5> server3:swap_code(name_server, new_name_server).
    ack

现在我们就可以调用新接口了：

    :::erl
    6> new_name_server:all_names().
    [joe,helen]


这里我们更新回调模块on the fly —— 也就是动态代码升级，一切都是在你眼前发生的，并无什么黑魔法。

现在停下来再想一想。最后两个任务我们一般认为是困难的，事实上，是非常困难。支持事务处理语义的代码很难写；支持代码热升级的server更加难写。

这项技术非常强大。传统上我们认为server是拥有状态的程序，并且我们可以给它发送消息改变其状态。一旦server上线后，它就是固定的了，如果我们想修改server的代码，我们不得不停止server，修改代码，然后再启动server。在上述示例中，我们可以不停止server而修改代码，就和修改server的状态一样容易。

Server 4: Even More Fun
------------------

既然我们已经可以让代码热更新了，我们还可以做到其它一些有趣的事情。下面的server什么也不做，直到你告诉它成为某种特定的server：

server4.erl

    :::erlang
    -module(server4).
    -export([start/0, rpc/2]).

    start() -> spawn(fun() -> wait() end).

    wait() ->
        receive
            {become, F} -> F()
        end.

    rpc(Pid, Q) ->
        Pid ! {self(), Q},
        receive
            {Pid, Reply} -> Reply
        end.


如果我们启动它，然后给它发送消息 `{become, F}`，它就会变成执行 `F()` 的 `F` server。我们来启动它：

    :::erl
    1> Pid = server4.start().
    <0.57.0>

这个server什么也不做，仅仅等待 `become` 消息。让我们来定义一个server函数吧。它很简单，仅仅来计算阶乘：

    :::erlang
    -module(my_fac_server).
    -export([loop/0]).

    loop() ->
        receive
            {From, {fac, N}} ->
                From ! {self(), fac(N)},
                loop();
            {become, Something} ->
                Something()
        end.

    fac(0) -> 1;
    fac(N) -> N * fac(N - 1).


现在我们可以让上面server来做一个计算阶乘的server了：

    :::erl
    2> c(my_fac_server).
    {ok,my_fac_server}
    3> Pid ! {become, fun my_fac_server:loop/0}.
    {become,#Fun<my_fac_server.loop.0>}

好了，它已经变成阶乘server了，我们可以这样：

    :::erl
    4> server4:rpc(Pid, {fac, 30}).
    265252859812191058636308480000000

它会一直是一个阶乘server，直到我们给它发送 `{become, Something}` 让它变成其它server。

小结
----

如上述几个例子所示，我们可以用不同的语法和一些奇妙的属性实现不同类型的server。这个技术几乎太强大了。利用所有潜力，它可以使一个小程序变得惊人强大与优雅。但当我们几十个人在做一个工业级的工程时，也许不想让事情变得太过动态。我们不得不试图在强大与通用之间寻求平衡。可以热更新的代码很漂亮，但一旦出了问题，调试起来会是个噩梦。在我们做了十几次动态升级后突然crash的话，想找出哪出错了不太容易。

在这一小节中所示的这些例子实际上并不十分正确。它们被写成这个样子是为了描述其所包含的思想，但它们确有一两个非常小但明显的错误。我不会立马告诉你是什么样的错误，但在这一章结束前我会给出一些提示。

The Erlang module `gen_server` is the kind of logical conclusion of a succession of successively sophisticated servers (just like the ones we’ve written so far in this chapter).


节译自 《[Programming Erlang](http://www.amazon.com/Programming-Erlang-Software-Concurrent-World/dp/193435600X)》。
