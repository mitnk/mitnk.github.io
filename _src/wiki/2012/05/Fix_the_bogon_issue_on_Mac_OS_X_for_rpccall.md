For the following code:

    :::erlang
    -module(kvs).
    -export([start/0, store/2, lookup/1]).

    start() -> register(kvs, spawn(fun() -> loop() end)).

    store(Key, Value) -> rpc({store, Key, Value}).

    lookup(Key) -> rpc({lookup, Key}).

    rpc(Request) ->
        kvs ! {self(), Request},
        receive
            {kvs, Response} ->
                Response
        end.

    loop() ->
        receive
            {From, {lookup, Key}} ->
                Value = get(Key),
                From ! {kvs, Value},
                loop();
            {From, {store, Key, Value}} ->
                put(Key, Value),
                From ! {kvs, ok},
                loop()
        end.

When we start a shell to run:

    :::erl
    $ erl -sname tom
    (tom@bogon)1> kvs:start().
    true

Then we start a second shell to run:

    :::erl
    $ erl -sname cat
    (cat@bogon)1> rpc:call(tom@bogon, kvs, store, [name, hi]).

But it doesn't work.

We can add the follow code into `/etc/hosts` to fix this problem.

    127.0.0.1	bogon

Done.