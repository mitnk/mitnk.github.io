Erlang Sequential Programming
=============================


**Simple Integer Arithmetic**

    :::erl
    1> 2 + 3 * 4.
    14

**Base 16 and base 32 notation**

    :::erl
    1> 2#111 * 10#3.
    21
    2> 16#cafe * 32#sugar.
    1577682511434
    3> 36#z.  %% 36, 10 + 26, is the biggest
    35

**Variables**

    :::erl
    1> X = 1234567.
    1234567
    2> X.
    1234567
    3> X * X * X.
    1881672302290562263
    4> X = 1234.
    ** exception error: no match of right hand side value 1234

**Floating-Point Numbers**

    :::erl
    1> 5 / 3.
    1.66667
    2> 4 / 2.
    2.00000
    3> 5 div 3.
    1
    4> 5 rem 3.
    2
    5> 4 div 2.
    2

**Boolean and Comparison**

    :::erl
    7> 5 =:= 5.0.
    false
    8> 5 == 5.0.
    true
    9> 5 /= 5.0.
    false
    10> 5 =/= 5.0.
    true
    11> true and false.
    false
    12> true or false.
    true
    14> true xor false.
    true
    15> not false.
    true
    16> 1 >= 1.
    true
    17> 1 =< 1.
    true
    18> 1 < false.
    true
    19> % number < atom < reference < fun < port < pid < tuple < list < bit string


**Atoms**

    :::erl
    1> hello.
    hello

Like `define` in C:

    :::c
    #define NULL 0

Atoms start with lowercase letters, followed by a sequence of alphanumeric chars or the _ or @ sign.
Atoms can also be quoted with `'` char, e.g. 'Name', '+', 'Hello', or 'a'

    :::erl
    1> 'Name'.
    'Name'
    2> 'a'.
    a
    3> 'a' == a.
    true

**Tuples**

Like struct in C:

    :::c
    struct point {
      int x;
      int y;
    } P;
    P.x = 10; P.y = 45;


In Erlang it is:

    :::erl
    1> P = {10, 45}
    {10,45}
    2> Point = {point, 10, 45}.
    {point,10,45}
    3> {point, X, Y} = Point.
    {point,10,45}
    4> X.
    10
    5> Y.
    45
    6> {_, _, Y2} = Point.
    {point,10,45}
    7> Y2.
    45

The number of elements is said to be the size of the tuple.

    :::erl
    1> tuple_size({a, b, c, d, 20}).
    5

**2.10 Lists**

    :::erl
    1> L = [1, 3, 5].
    [1,3,5]
    2> ThingsToBuy = [{apples, 10}, {pears, 6}, {milk, 3}].
    [{apples, 10},{pears,6},{milk,3}]
    3> [H|T] = L.
    [1,3,5]
    4> H.
    1
    5> T.
    [3,5]
    6> f().
    ok
    7> [H1, H2 | T] = [1,3,5,7,9].
    [1,3,5,7,9]
    8> {H1, H2, T}
    {1, 3, [5,7,9]}
    9> [1, 2, 3] ++ [4, 5].
    [1,2,3,4,5]
    10> [1, 2, 3] -- [1, 2].
    [3]
    19> hd([1, 2, 3]).
    1
    20> tl([1, 2, 3]).
    [2,3]
    21> [2*N || N <- [1,2,3,4]].
    [2,4,6,8]
    22> [X || X <- [1,2,3,4,5,6,7,8,9,10], X rem 2 =:= 0].
    [2,4,6,8,10]

built-in functions (BIFs) are usually functions that could not be implemented in pure Erlang.

**Strings**

There are no strings in Erlang. They are the list of integers.

    :::erl
    1> Name = "Hello".
    "Hello"
    2> [83,117,114,112,114,105,115,101].
    "Surprise"
    3> [1,83,117,114,112,114,105,115,101].
    [1,83,117,114,112,114,105,115,101]

Dollar syntax

    :::erl
    1> I = $s.
    115
    2> [I-32,$u,$r,$p,$r,$i,$s,$e].
    "Surprise"

**Bit Syntax**

    :::erl
    1> Color = 16#F09A29.
    15768105
    2> Pixel = <<Color:24>>.
    <<240,154,41>>
    3> <<R:8, G:8, B:8>> = Pixel.
    <<240,154,41>>
    4> R.
    240
    5> <<R1:8, _/binary>> = Pixel.
    <<240,154,41>>
    6> <<R2:16, _/binary>> = Pixel.
    <<240,154,41>>
    7> R2.
    61594
    18> R2 = <<240,154>>.  % R2 is an integer, not a binary.
    ** exception error: no match of right hand side value <<240,154>>
    20> is_binary(R2).
    false
    21> is_integer(R2).
    true
    19> <<R2:16>> = <<240,154>>.
    <<240,154>>
    8> binary_to_list(R2).
    [240,154]

    **More Binary Stuff**
    1> <<Port1:16/integer-signed-big>> = <<1,2>>.
    <<1,2>>
    2> Port1.
    258
    3> <<Port2:16/integer-signed-little>> = <<1,2>>.
    <<1,2>>
    4> Port2.
    513

Type: integer | float | binary | bytes | bitstring | bits | utf8 | utf16 | utf32
Signedness: signed | unsigned
Endianness: big | little | native

The standard binary operations (shifting bits to left and right,
binary 'and', 'or', 'xor', or 'not') also exist in Erlang.
Just use the functions bsl (Bit Shift Left), bsr (Bit Shift Right),
band, bor, bxor, and bnot. e.g. `2#00100 = 2#00010 bsl 1.`

One could parse TCP segments with code like this:

    :::erl
    <<SourcePort:16, DestinationPort:16,
      AckNumber:32,
      DataOffset:4, _Reserved:4, Flags:8, WindowSize:16,
      CheckSum: 16, UrgentPointer:16,
      Payload/binary>> = SomeBinary.

**Binary Comprehensions**

    :::erl
    1> [ X || <<X>> <= <<1,2,3,4,5>>, X rem 2 == 0].
    [2,4]
    2> Pixels = <<213,45,132,64,76,32,76,0,0,234,32,15>>.
    <<213,45,132,64,76,32,76,0,0,234,32,15>>
    3> RGB = [{R,G,B} || <<R:8,G:8,B:8>> <= Pixels].
    [{213,45,132},{64,76,32},{76,0,0},{234,32,15}]
    4> << <<R:8,G:8,B:8>> || {R,G,B} <- RGB >>.
    <<213,45,132,64,76,32,76,0,0,234,32,15>>
    5> << <<(X+1)/integer>> || <<X>> <= <<3,7,5,4,7>> >>.
    <<4,8,6,5,8>>

Via: [http://learnyousomeerlang.com/starting-out-for-real#bit-syntax](http://learnyousomeerlang.com/starting-out-for-real#bit-syntax)

**Get Help**

    :::erl
    $ erl -man lists


Chapter 3 Sequential Programming
--------------------------------

**3.1 Modules**

Modules are the basic unit of code in Erlang. All the functions we write are stored in modules.

    :::erlang
    -module(geometry).
    -export([area/1]).
    area({rectangle, Width, Ht}) -> Width * Ht;
    area({square, X}) -> X * X;
    area({circle, R}) -> 3.14159 * R * R.

Usage

    :::erl
    $ erl
    1> c(geometry).
    {ok,geometry}
    2> geometry:area({rectangle, 10, 5}).
    50
    3> geometry:area({circle, 1.4}).
    6.15752


**3.3 Functions with the same name and different Arity**

    :::erlang
    sum(L) -> sum(L, 0).

    sum([], N) -> N;
    sum([H|T], N) -> sum(T, H+N).


**3.4 Funs**

funs are anonymous functions.

    :::erl
    1> Z = fun(X) -> 2 * X end.
    #Fun<erl_eval.6.34545567>
    2> Z(2).
    4
    3> Double = Z.
    #Fun<erl_eval.6.30202343>
    4> Double(4).
    8
    5> Temp = fun({c, C}) -> {f, 32 + C*9/5};
    5>        ({f, F}) -> {c, (F-32) * 5 / 9}
    5>        end.
    #Fun<erl_erval.6.56003434>
    6> Temp({f, 212}).
    {c,100.000}

Defining Your Own Control Abstractions

    :::erlang
    for(Max, Max, F) -> [F(Max)];
    for(I, Max, F) -> [F(I) | for(I + 1, Max, F)].


`for(1, 10, F)` creates he list `[F(1),F(2), ..., F(10)]`.

**3.6 List Comprehensions**

    :::erl
    1> L = [1,2,3,4,5].
    [1,2,3,4,5]
    2> lists:map(fun(X) -> 2*X end, L).
    [2,4,6,8,10]
    3> [2*X || X <- L].
    [2,4,6,8,10]


Quicksort

    :::erlang
    qsort([]) -> [];
    qsort([Pivot|T]) ->
        qsort([X || X <- T, X < Pivot])
        ++ [Pivot] ++
        qsort([X || X <- T, X >= Pivot]).


Pythagorean Triplets

    :::erlang
    pythag(N) ->
        [{A, B, C} ||
            A <- lists:seq(1, N),
            B <- lists:seq(1, N),
            C <- lists:seq(1, N),
            A + B + C =< N,
            A*A + B*B =:= C*C
        ].

Usage

    :::erl
    1> pythag(30).
    [{3,4,5},{5,12,13},{6,8,10}]


Anagrams

`X--Y` is the list subtraction operator. It subtracts the elements in Y from X

    :::erlang
    perms([]) -> [[]];
    perms(L) -> [[H|T] || H <- L, T <- perms(L--[H])].

Usage

    :::erl
    1> lib_misc:perms("234").
    ["234","243","324","342","423","432"]


List Operations `++` and `--`

    :::erl
    1> [1, 2, 3] ++ [4, 5, 6].
    [1,2,3,4,5,6]
    2> [a,b,1,c,1,d,1] -- [1].
    [a,b,c,1,d,1]
    3> [a,b,1,c,1,d,1] -- [1,1].
    [a,b,c,d,1]
    4> [a,b,1,c,1,d,1] -- [1,1,1].
    [a,b,c,d]
    3> [a,b,1,c,1,d,1] -- [1,1,1,1].
    [a,b,c,d]


**3.7 Arithmetic Expressions**

    :::
    +X
    -X
    X*Y
    X/Y (floating-point division)
    bnot X (Bitwise not of X)
    X div Y (Integer division of X and Y)
    X rem Y (Integer remainder of X divided by Y)
    X band Y (Bitwise and of X and Y)
    X+Y
    X-Y
    X bor Y (Bitwise or of X and Y)
    X bxor Y (Bitwise xor of X and Y)
    X bsl N (Arithmetic bitshift left of X by N bits)
    X bsr N (Bitshift right of X by N bits)


**3.8 Guards**

    :::erlang
    max(X, Y) when X > Y -> X;
    max(X, Y) -> Y.


Examples

    :::erlang
    f(X, Y) when is_integer(X), X > Y, Y < 6 -> ...

    is_tuple(T), size(T) =:= 6, abs(element(3, %)) > 5

    element(4, X) =:= hd(L)

    A >= -1.0 andalso A+1 > B

    is_atom(L) orelse (is_list(L) andalso length(L) > 2)

The comma, which separates the test in the guard, means "and".

Guard predicates

    :::erlang
    is_atom(X)
    is_binary(X)
    is_constant(X)
    is_float(X)
    is_function(X)
    is_function(X, N)
    is_integer(X)
    is_list(X)
    is_number(X)
    is_pid(X)
    is_port(X)
    is_reference(X)
    is_tuple(X)
    is_record(X,Tag)
    is_record(X,Tag,N)


The True Guard

    :::erlang
    if
      Guard -> Expressions;
      Guard -> Expressions;
      ...
      true -> Expressions
    end


Guard built-in functions

    :::
    abs(X)
    Absolute value of X.

    element(N,X)
    Element N of X. Note X must be a tuple.

    float(X)
    Convert X, which must be a number, to a float.

    hd(X)
    The head of the list X.

    length(X)
    The length of the list X.

    node()
    The current node.

    node(X)
    The node on which X was created.  X can be a process.
    An identifier, a reference, or a port.

    round(X)
    Converts X, which must be a number, to an integer.

    self()
    The process identifier of the current process.

    size(X)
    The size of X. X can be a tuple or a binary.

    trunc(X)
    Truncates X, which must be a number, to an integer.

    tl(X)
    The tail of the list X.


**3.9 Records**

Records provide a method for associating a name with a particular element in a tuple.

in records.hrl

    :::erlang
    -record(todo, {status=reminder, who=joe, text})

Usage

    :::erl
    1> rr("records.hrl").
    [todo]
    2> X=#todo{}.
    #todo{status = reminder,who = joe,text = undefined} 
    3> X1 = #todo{status=urgent, text="Fix errata in book"}.
    #todo{status = urgent,who = joe,text = "Fix errata in book"} 
    4> X2 = X1#todo{status=done}.
    #todo{status = done,who = joe,text = "Fix errata in book"}
    5> X2#todo.text.
    "Fix errata in book"


3.10 case and if Expressions

    :::erlang
    case Expression of
        Pattern1 [when Guard1] -> Expr_seq1;
        Pattern2 [when Guard2] -> Expr_seq2;
        ...
    end


Function filter(P, L) returns a list of all those elements X in L
for which P(X) is true.

    :::erlang
    filter(P, [H|T]) -> filter1(P(H), H, P, T);
    filter(P, []) -> [].

    filter1(true, H, P, T) -> [H|filter(P, T)];
    filter1(false, H, P, T) -> filter(P, T).


Using case expression:

    :::erlang
    filter(P, [H|T]) ->
        case P(H) of
            true -> [H|filter(P, T)];
            flase -> filter(P, T)
        end;
    filter(P, []) ->
        [].


if Expressions

    :::erlang
    if
        Guard1 ->
            Expr_seq1;
        Guard2 ->
            Expr_seq2;
        ...
        true ->
            Expr_final;
    end


At least one of the guards in the if expression must evaluate to true; otherwise, an exception will be raised.
