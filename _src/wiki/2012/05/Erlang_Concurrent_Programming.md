Chapter 8 Concurrent Programming

In Erlang, processes belong to the programming language and NOT the operating system.

In Erlang:

- Creating and destroying processes is very fast.
- Sending messages between processes is very fast.
- Processes behave the same way on all operating systems.
- We can have very large numbers of processes.
- Processes share no memory and are completely independent.
- The only way for processes to interact is through message passing.

For these reasons Erlang is sometimes called a pure message passing language.

    :::erlang
    -module(area_server0).
    -export([loop/0]).

    loop() ->
        receive
            {rectangle, Width, Ht} ->
                io:format("Area of rectangle is ~p~n", [Width * Ht]),
                loop();
            {circle, R} ->
                io:format("Area of circle is ~p~n", [3.14159 * R * R]),
                loop();
            Other ->
                io:format("I don't know what the area of a ~p is ~n", [Other]),
                loop()
        end.

We can create a process that evaluates loop/0 in the shell:

    :::erl
    1> Pid = spawn(fun area_server0:loop/0).
    <0.36.0>
    2> Pid ! {rectangle, 6, 10}.
    Area of rectangle is 60
    {rectangle,6,10}
    3> Pid ! {circle, 23}.
    Area of circle is 1661.90
    {circle,23}
    4> Pid ! {triangle,2,4,5}.
    I don't know what the area of a {triangle,2,4,5} is {triangle,2,4,5}

A better pattern to write a server:

    :::erlang
    -module(area_server_final).
    -export([start/0, area/2]).

    start() -> spawn(fun loop/0).

    area(Pid, What) ->
        rpc(Pid, What).

    rpc(Pid, Request) ->
        Pid ! {self(), Request},
        receive
            {Pid, Response} ->
                Response
        end.

    loop() ->
        receive
            {From, {rectangle, Width, Ht}} ->
                From ! {self(), Width * Ht},
                loop();
            {From, {circle, R}} ->
                From !  {self(), 3.14159 * R * R},
                loop();
            {From, Other} ->
                From ! {self(), {error,Other}},
                loop()
        end.

rpc short for remote pro- cedure call.

Implementing a Timer

    :::erlang
    -module(stimer).
    -export([start/2, cancel/1]).

    start(Time, Fun) -> spawn(fun() -> timer(Time, Fun) end).

    cancel(Pid) -> Pid ! cancel.

    timer(Time, Fun) ->
    receive
        cancel ->
            void
        after Time ->
            Fun()
    end.

Test it:

    :::erl
    1> Pid = stimer:start(5000, fun() -> io:format("timer event~n") end).
    <0.42.0>
    timer event

receive works as follows:

1. When we enter a receive statement, we start a timer
(but only if an after section is present in the expression).

2. Take the first message in the mailbox and try to match it against Pattern1,
Pattern2, and so on. If the match succeeds, the message is removed from
the mailbox, and the expressions following the pattern are evaluated.

3. If none of the patterns in the receive statement matches the first message
in the mailbox, then the first message is removed from the mailbox and put
into a “save queue.” The second message in the mailbox is then tried.
This procedure is repeated until a matching message is found or until
all the messages in the mail- box have been examined.

4. If none of the messages in the mailbox matches, then the process is
suspended and will be rescheduled for execution the next time a new
message is put in the mailbox. Note that when a new message arrives,
the messages in the save queue are not rematched; only the new message
is matched.

5. As soon as a message has been matched, then all messages that have been
put into the save queue are reentered into the mailbox in the order in which
they arrived at the process. If a timer was set, it is cleared.

6. If the timer elapses when we are waiting for a message, then evaluate
the expressions ExpressionsTimeout and put any saved messages back into
the mailbox in the order in which they arrived at the process.


Registered processes

    :::erlang
    -module(clock).
    -export([start/2, stop/0]).

    start(Time, Fun) ->
        register(clock, spawn(fun() -> tick(Time, Fun) end)).

    stop() -> clock ! stop.

    tick(Time, Fun) ->
        receive
            stop ->
                void
            after Time -> Fun(),
                tick(Time, Fun)
        end.

Test it:

    :::erl
    3> clock:start(5000, fun() -> io:format("TICK ~p~n",[erlang:now()]) end).
    true
    TICK {1164,553538,392266}
    TICK {1164,553543,393084}
    TICK {1164,553548,394083}

Pattern of writing Concurrent Programs:

    :::erlang
    -module(ctemplate).
    -compile(export_all).

    start() ->
        spawn(fun() -> loop([]) end).

    rpc(Pid, Request) ->
        Pid ! {self(), Request},
            receive
                {Pid, Response} ->
                    Response
            end.

    loop(X) ->
        receive
            Any ->
            io:format("Received:~p~n" ,[Any]), loop(X)
        end.
