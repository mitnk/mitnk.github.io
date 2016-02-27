A socket is a communication endpoint that allows machines to communicate over the Internet using the Internet Pro- tocol (IP).
There are two main libraries for programming with sockets: `gen_tcp` and `gen_upd`.

Using TCP
-------------

**Fetching Data from a Server**

    :::erlang
    -module(download_page).
    -export([get_url/1]).


    get_url(Host) ->
        {ok, Socket} = gen_tcp:connect(Host, 80, [binary, {packet, 0}]),
        ok = gen_tcp:send(Socket, "GET / HTTP/1.0\r\n\r\n"),
        receive_data(Socket, []).

    receive_data(Socket, SoFar) ->
        receive
            {tcp, Socket, Bin} ->
                receive_data(Socket, [Bin|SoFar]);
            {tcp_closed, Socket} ->
                list_to_binary(lists:reverse(SoFar))
        end.




Test:

    :::erl
    1> B = download_page:get_url("mitnk.com").
    <<"HTTP/1.1 301 Moved Permanently\r\nServer: nginx/1.0.12\r\nDate: Sat, 19 May 2012 10:56:06 GMT\r\nContent-Type: text/html\r\n"...>>
    2> io:format("~p~n", [B]).
    <<"HTTP/1.1 301 Moved Permanently\r\nServer: nginx/1.0.12\r\nDate: Sat, 19 May 2012 10:56:06 GMT\r\nContent-Type: text/html\r\nContent-Length: 185\r\nConnection: close\r\nLocation: http://mitnk.com/\r\n\r\n<html>\r\n<head><title>301 Moved Permanently</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>301 Moved Permanently</h1></center>\r\n<hr><center>nginx/1.0.12</center>\r\n</body>\r\n</html>\r\n">>
    ok
    3> string:tokens(binary_to_list(B), "\r\n").
    ["HTTP/1.1 301 Moved Permanently","Server: nginx/1.0.12",
     "Date: Sat, 19 May 2012 10:56:06 GMT",
     "Content-Type: text/html","Content-Length: 185",
     "Connection: close","Location: http://mitnk.com/","<html>",
     "<head><title>301 Moved Permanently</title></head>",
     "<body bgcolor=\"white\">",
     "<center><h1>301 Moved Permanently</h1></center>",
     "<hr><center>nginx/1.0.12</center>","</body>","</html>"]

You might think that it would be better to write the code to accumulate the fragments like this:

    :::erlang
    receive_data(Socket, SoFar) ->
    receive
        {tcp,Socket,Bin} ->
            receive_data(Socket, list_to_binary([SoFar,Bin]));
        {tcp_closed,Socket} ->
            SoFar
    end.

This code is correct but less efficient than the original version. The reason is that in the latter version we are continually appending a new binary to the end of the buffer, which involves a lot of copying of data. It’s much better to accumulate all the fragments in a list (which will end up in the wrong order) and then reverse the entire list and concatenate all the fragments in one operation.

A Simple TCP Server
---------------------

    :::erlang
    -module(nano_server).
    -export([start/0]).

    start() ->
        {ok, Listen} = gen_tcp:listen(2345,
                                      [binary, {packet, 0},
                                      {reuseaddr, true},
                                      {active, true}]),
        {ok, Socket} = gen_tcp:accept(Listen),
        gen_tcp:close(Listen),
        loop(Socket).

    loop(Socket) ->
        receive
            {tcp, Socket, <<"bye\r\n">>} ->
                gen_tcp:send(Socket, <<"bye\r\n">>),
                gen_tcp:close(Socket),
                ok;
            {tcp, Socket, Bin} ->
                io:format("Server received binary = ~p~n", [Bin]),
                Prefix = <<"you said: ">>,
                Reply = <<Prefix/binary, Bin/binary>>,
                gen_tcp:send(Socket, Reply),
                loop(Socket);
            {tcp_closed, Socket} ->
                io:format("client closed~n");
            X ->
                io:format("Got Unexpected Data: ~p ~n", [X])
        end.

This is the simplest of servers that illustrates how to package and encode the application data. It accepts a request, computes a reply, sends the reply, and terminates.

P.S. Use `telnet` to test this server.

Client in Erlang:

    :::erlang
    -module(nano_client).
    -export([connect/1]).

    connect(Str) ->
        {ok, Socket} = gen_tcp:connect("localhost", 2345, [binary, {packet, 0}]),
        ok = gen_tcp:send(Socket, Str),
        receive
            {tcp, Socket, Bin} ->
                io:format("Client received binary = ~p~n", [Bin]),
                gen_tcp:close(Socket)
        end.


Run server first, then use client to test it:

    :::erl
    1> nano_client:connect("Hello from nano client").


**A Parallel Server**

    :::erlang
    -module(nano_server).
    -export([start/0]).

    start() ->
        {ok, Listen} = gen_tcp:listen(2345,
                                      [binary, {packet, 4},
                                      {reuseaddr, true},
                                      {active, true}]),
        spawn(fun() -> par_connect(Listen) end).

    par_connect(Listen) ->
        {ok, Socket} = gen_tcp:accept(Listen),
        spawn(fun() -> par_connect(Listen) end),
        loop(Socket).

    loop(Socket) ->
        receive
            {tcp, Socket, Bin} ->
                io:format("Server received binary = ~p~n", [Bin]),
                Str = binary_to_term(Bin),
                io:format("server (unpacked) ~p~n", [Str]),
                Reply = {ok, "I got it.", Str},
                io:format("Server replying = ~p~n", [Reply]),
                gen_tcp:send(Socket, term_to_binary(Reply)),
                loop(Socket);
            {tcp_close, Socket} ->
                io:format("Server socket closed~n")
        end.


After we have accepted a connection, it’s a good idea to explicitly set the required socket options, like this:

    :::erlang
    {ok, Socket} = gen_tcp:accept(Listen),
    inet:setopts(Socket, [{packet,4},binary,
                       {nodelay,true},{active, true}]),
    loop(Socket)

Error Handling with Sockets
------------------

Error handling with sockets is extremely easy—basically you don’t have to do anything. As we said earlier, each socket has a controlling process (that is, the process that created the socket). If the controlling process dies, then the socket will be automatically closed.

This means that if we have, for example, a client and a server and the server dies because of a programming error, the socket owned by the server will be automatically closed, and the client will be sent a {tcp_closed, Socket} message.


UDP
-----

Writing a UDP client and server in Erlang is much easier than writ- ing in the TCP case since we don’t have to worry about maintaining connections to the server.

    :::erlang
    -module(udp_server).
    -export([start/0]).

    start() ->
        {ok, Socket} = gen_udp:open(2345, [binary]),
        loop(Socket).

    loop(Socket) ->
        receive
            {udp, Socket, Host, Port, Bin} ->
                N = binary_to_term(Bin),
                Fac = fac(N),
                gen_udp:send(Socket, Host, Port, term_to_binary(Fac)),
                loop(Socket)
        end.

    fac(0) -> 1;
    fac(N) -> N * fac(N - 1).

Client side:

    :::erlang
    -module(udp_client).
    -export([conn/1]).

    conn(Request) ->
        {ok, Socket} = gen_udp:open(0, [binary]),
        ok = gen_udp:send(Socket, "localhost", 2345, term_to_binary(Request)),
        Value = receive
                {udp, Socket, _, _, Bin} ->
                    {ok, binary_to_term(Bin)}
                after 2000 ->
                    error
                end,
        gen_udp:close(Socket),
        Value.


**Additional Notes on UDP**

A UDP packet can be delivered twice (which surprises some people), so you have to be careful writing code for remote procedure calls. It might happen that the reply to a second query was in fact a duplicated answer to the first query. To avoid this, we could modify the client code to include a unique reference and check that this reference is returned by the server.

    :::erlang
    client(Request) ->
        {ok, Socket} = gen_udp:open(0, [binary]),
        Ref = make_ref(), %% make a unique reference
        B1 = term_to_binary({Ref, Request}),
        ok = gen_udp:send(Socket, "localhost", 4000, B1),
        wait_for_ref(Socket, Ref).

    wait_for_ref(Socket, Ref) ->
        receive
            {udp, Socket, _, _, Bin} ->
                case binary_to_term(Bin) of
                    {Ref, Val} ->
                         %% got the correct value
                         Val;
                    {_SomeOtherRef, _} ->
                        %% some other value throw it away
                        wait_for_ref(Socket, Ref)
                end;
        after 1000 ->
            ...
        end.




Broadcasting to Multiple Machines
--------------------

For completeness, I’ll show you how to set up a broadcast channel. This code is rather rare, but one day you might need it.

    :::erlang
    -module(broadcast).
    -compile(export_all).

    send(IoList) ->
        case inet:ifget("eth0", [broadaddr]) of
            {ok, [{broadaddr, Ip}]} ->
                {ok, S} =  gen_udp:open(5010, [{broadcast, true}]),
                gen_udp:send(S, Ip, 6000, IoList),
                gen_udp:close(S);
            _ ->
                io:format("Bad interface name, or\n"
                          "broadcasting not supported\n")
        end.

    listen() ->
        {ok, S} = gen_udp:open(6000),
        loop(S).

    loop(S) ->
        receive
            Any ->
                io:format("received:~p~n", [Any]),
                loop(S)
        end.


Digging Deeper
-------------

We have looked at only the most commonly used functions for manipulating sockets. You can find more information about the socket APIs in the manual pages for gen_tcp, gen_udp, and inet.
