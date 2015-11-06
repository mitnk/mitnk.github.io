**What does exception look like?**

    :::erlang
    -module(shop).
    -export([cost/1]).

    cost(apple) -> 2;
    cost(orange) -> 3.


This is what happened when we ran it:

    :::erl
    1> shop:cost(apple).
    2
    2> shop:cost(pear).
    ** exception error: no function clause matching shop:cost(pear) (shop.erl, line 4)

**Raising an Exception:**


`exit(Why)`

This is used when you really want to terminate the current process.
If this exception is not caught, the message `{’EXIT’,Pid,Why}` will be
broadcast to all processes that are linked to the current process.

`throw(Why)`

This is used to throw an exception that a caller might want to catch.
In this case we document that our function might throw this exception.

`erlang:error(Why)`

This is used for denoting “crashing errors.” That is, something rather
nasty has happened that callers are not really expected to handle.
This is on par with internally generated errors.

**try...catch Syntax**

    :::erlang
    try FuncOrExpressionSequence of
        Pattern1 [when Guard1] -> Expressions1;
        Pattern2 [when Guard2] -> Expressions2;
        ...
    catch
        ExceptionType: ExPattern1 [when ExGuard1] -> ExExpressions1;
        ExceptionType: ExPattern2 [when ExGuard2] -> ExExpressions2;
        ...
    after
        AfterExpressions
    end

Example:

    :::erlang
    generate_exception(1) -> a;
    generate_exception(2) -> throw(a);
    generate_exception(3) -> exit(a);
    generate_exception(4) -> {'EXIT', a};
    generate_exception(5) -> erlang:error(a).

    demo1() ->
        [catcher(I) || I <- [1,2,3,4,5]].

    catcher(N) ->
        try generate_exception(N) of
            Val -> {N, normal, Val}
        catch
            throw:X -> {N, caught, thrown, X};
            exit:X  -> {N, caught, exited, X};
            error:X -> {N, caught, error, X}
        end.

Run it:

    :::erl
    1> try_test:demo1().
    [{1,normal,a},
     {2,caught,thrown,a},
     {3,caught,exited,a},
     {4,normal,{'EXIT',a}},
     {5,caught,error,a}]

The other way to trap an exception is to use the primitive catch.  When you
catch an exception, it is converted into a tuple that describes the error.

    :::erlang
    demo2() ->
        [{I, (catch generate_exception(I))} || I <- [1,2,3,4,5]].

Run it:

    :::erl
    2> try_test:demo2().
    [{1,a},
     {2,a},
     {3,{'EXIT',a}},
     {4,{'EXIT',a}}, {5,{'EXIT',{a,[{try_test,generate_exception,1},
                     {try_test,'-demo2/0-fun-0-',1},
                     {lists,map,2},
                     {lists,map,2},
                     {erl_eval,do_apply,5},
                     {shell,exprs,6},
                     {shell,eval_loop,3}]}}}]

**Catching Every Possible Exception**

    :::erlang
    try Expr catch
        _:_ -> ... Code to handle all exceptions  ...
    end

(End of Exception)

----

Errors in Concurrent Programs
-----------------------------

Error handling in concurrent Erlang programs is based on the idea of
*remote detection and handling of errors*. Instead of handling an error
in the process where the error occurs, we let the process die and
correct the error in some other process.

The Erlang philosophy for building fault-tolerant software can be
summed up in two easy-to-remember phrases: “Let some other process
fix the error” and “Let it crash.”

**Linking Processes**

Processes can be linked. If the two processes A and B are linked and
A terminates for any reason, an error signal will be sent to B and
the other way around.

**Monitors** are similar to links but are one-directional. If A monitors B
and if B terminates for any reason, a “down” message will be sent to A
but not the other way around.

If the receiver hasn’t taken any special steps, the exit signal will cause it,
too, to exit. However, a process can ask to trap these exit signals. When a
process is in this state, it is called a *system process*.

**An `on_exit` Handler**

    :::erlang
    on_exit(Pid, Fun) ->
        spawn(fun() ->
            process_flag(trap_exit, true),
            link(Pid),
            receive
                {'EXIT', Pid, Why} ->
                    Fun(Why)
            end
        end).

In line 3, the statement process_flag(trap_exit, true) turns the spawned
process into a system process. link(Pid) (line 4) links the newly spawned
process to Pid. Finally, when the process dies, an exit signal is received
(line 6) and processed (line 7).

Test it:

    :::erl
    1> F = fun() -> receive
                X -> list_to_atom(X)
            end
        end.
    #Fun<erl_eval.20.69967518>

    % We’ll spawn this:
    2> Pid = spawn(F).
    <0.61.0>

    % And we’ll set up an on_exit handler to monitor it:
    3> lib_misc:on_exit(Pid,
                        fun(Why) ->
                            io:format(" ~p died with:~p~n",[Pid, Why])
                        end).
    <0.63.0>

    %% If we send an atom to Pid, the process will die (because it tries to
    %% evaluate list_to_atom of a nonlist), and the on_exit handler will be called:
    4> Pid ! hello.
    hello
    <0.61.0> died with:{badarg,[{erlang,list_to_atom,[hello]}]}

**Programming Idioms for Trapping Exits**

Idiom 1: I Don’t Care If a Process I Create Crashes

    :::erlang
    Pid = spawn(fun() -> ... end)

Idiom 2: I Want to Die If a Process I Create Crashes

    :::erlang
    Pid = spawn_link(fun() -> ... end)

Idiom 3: I Want to Handle Errors If a Process I Create Crashes

    :::erlang
    ...
    process_flag(trap_exit, true),
    Pid = spawn_link(fun() -> ... end),
    ...
    loop(...).

    loop(State) ->
        receive
            {'EXIT', SomePid, Reason} ->
                  %% do something with the error
                  loop(State1);
            ...
        end

**A Keep-Alive Process**

    :::erlang
    keep_alive(Name, Fun) ->
        register(Name, Pid = spawn(Fun)),
        on_exit(Pid, fun(_Why) -> keep_alive(Name, Fun) end).

This makes a registered process called Name that evaluates spawn(Fun).
If the process dies for any reason, then it is restarted.

There is a possibility the process dies in the gap between these two statements.
If the process dies before on_exit gets evaluated, then no link will be created,
and the on_exit process will not work as you ex- pected. This could happen if
two programs try to evaluate keep_alive at the same time and with the same
value of Name. This is called a `race condition`.

