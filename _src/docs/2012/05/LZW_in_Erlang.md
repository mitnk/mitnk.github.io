[LZW算法](http://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)是Terry Welch在1978年发表的一个无损数据压缩算法。这个算法基于Abraham Lempel和Jacob Ziv发表的算法[LZ77, LZ78](http://en.wikipedia.org/wiki/LZ77_and_LZ78)。LZ77是后来很多压缩算法（如gzip等）的基础，且被命名为[IEEE里程碑之一](http://en.wikipedia.org/wiki/List_of_IEEE_milestones)。

在写LZW之前先看一看最简单的一种数据压缩算法RLE（[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding)）。比如一个拥有白色背景黑色文字的屏幕，我们可以将之“序列化”成如下字符串：

    WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

W代表白色，B为黑色。应用RLE算法后，字符串可以被压缩成这样：

    12W1B12W3B24W1B14W

下面是用Erlang给出的一个RLE实现。

    :::erlang
    -module(rle).
    -export([encode/1, decode/1, test/0]).

    encode(S) ->
        doEncode(S ++ [0], "", 1, []).

    doEncode([], _, _, Result) ->
        Result;

    doEncode([Next|S], Current, Count, Result) ->
        if
            Current =:= Next ->
                encode(S, Current, Count + 1, Result);
            Current =:= "" ->
                encode(S, Next, 1, Result);
            true ->
                encode(S, Next, 1, Result ++ [Count, Current])
        end.

    decode(E) ->
        if
            length(E) rem 2 =/= 0 -> error_param;
            true -> doDecode(E ++ [0, 0], [])
        end.

    doDecode([], Result) ->
        Result;

    doDecode([Count, Char|E], Result) ->
        if
            Count =:= 0 -> decode(E, Result);
            true -> decode([Count - 1, Char] ++ E, Result ++ [Char])
        end.


    test() ->
        S = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        E = encode(S),
        io:format("Original: ~p~n Encoded: ~p~nRate: ~p~n Check Decode:~p~n",
                  [S, E, length(E) / length(S), decode(E) =:= S]).

LZ算法把输入序列分成不同的片断，每个片断用前一个片断的引用和一些额外信息表示。一个简单实现是这个样子的：

      INPUT: The sequence to be compressed S over some finite alphabet of characters
      OUTPUT: A sequence of pairs (reference, character)
    A1 Search for the shortest block W that is not in the dictionary
    A2 if W is a single character c
    A3       encode W as (0, c)
    A4 else W is a phrase X that is in the dictionary plus a character c
    A5       encode W as (reference to X in D, c)
    A6 Add W to the dictionary
    A7 Go to step A1

而解压算法是这个的逆过程，很简单，这里就不列了，可以参考[Wikipedia](http://en.wikipedia.org/wiki/LZ77_and_LZ78)。

现在到LZW了。其压缩（encoding）过程是这样的：

1. 将输入序列中的每一个字符都放到字典里。
2. 找当前输入在字典中的最长序列`W`。
3. 输出`W`在字典中的索引，并将`W`从输入中去除。
4. 把`W`加上下一个字符放进字典。
5. 返回步骤2.

上Erlang代码：

    :::erlang
    -module(lzw).
    -export([compress/1, test/0]).
    -define(MIN_CODE, 256).

    compress(S) ->
        Dict = dict:new(),
        doCompress(S ++ [0], Dict, [], ?MIN_CODE, []).

    doCompress([], _, _, _, Result) ->
        Result;

    doCompress([Char|S], Dict, Buffer, Code, Result) ->
        case is_ascii_or_in_dict(Dict, Buffer ++ [Char]) of
            [] ->
                Index = is_ascii_or_in_dict(Dict, Buffer),
                NewResult = Result ++ listify(Index),
                NewDict = dict:append(Buffer ++ [Char], Code, Dict),
                doCompress(S, NewDict, [Char], Code + 1, NewResult);
            _ ->
                doCompress(S, Dict, Buffer ++ [Char], Code, Result)
        end.

    listify(Thing) when is_list(Thing) ->
        Thing;

    listify(Thing) ->
        [Thing].

    is_ascii_or_in_dict(Dict, [Item]) ->
        is_ascii_or_in_dict(Dict, Item);

    is_ascii_or_in_dict(Dict, Item) ->
        case dict:find(Item, Dict) of
            error ->
                if
                    ((Item >= 0) and (Item < ?MIN_CODE)) ->
                        Item;
                    true ->
                        []
                end;
            {ok, [Value]} ->
                Value
        end.


    test() ->
        S = "ABABABAB",
        compress(S).

用上面的算法压缩字符串`"ABABABAB"`得到的结果是`[A, B, 256, 258, B]`（注：[Erlang中的字符串即list](http://www.erlang.org/doc/reference_manual/data_types.html#id73373))。

解压（decoding）的过程是这样的 (方便起见我们将256, 257, ... 记为 0, 1, ... )：

<table border="1">
<tr>
    <th>Input|E</th><th>Output</th><th>Result</th><th>Conjecture</th><th>Add to Dict</th>
</tr>
<tr>
    <td>A|B02B</td><td>A</td><td>A</td><td>0: A+?</td><td>-</td>
</tr>
<tr>
    <td>B|02B</td><td>B</td><td>AB</td><td>1: B+?</td><td>0: AB</td>
</tr>
<tr>
    <td>0|2B</td><td>AB</td><td>ABAB</td><td>2: AB+?</td><td>1: BA</td>
</tr>
<tr>
    <td>2|B</td><td>?</td><td>ABAB?</td><td>2: AB+?</td><td>-</td>
</tr>
<tr>
    <td>2|B</td><td>ABA</td><td>ABABABA</td><td>3: ABA+?</td><td>2: ABA</td>
</tr>
<tr>
    <td>B|</td><td>B</td><td>ABABABAB</td><td>-</td><td>3: ABAB</td>
</tr>
</table>

在每一步中，decoder收到一个Code `X`并且在字典中查找到它的值`χ`输出到结果，同时推测`χ + ?`为字典中下一个索引的值——因为encoder将`X`生成`χ`的索引就是因为`χ + ?`不在字典中。但这个`?`到底是哪个字符呢？它是下一个Code `Z`所索引的值的第一个字符。所以decoder查找`Z`。

但如果`Z`还不在字典中怎么办？方案如下：

1. Decoder先看到`X`然后是`Z`。
2. 它知道索引`X`的值是`χ`，而索引`Z`的值为未知量`ω`。
3. 它知道encoder刚刚加入索引`Z`，其值为`χ`加上某个未知字符，
4. 且知道未知字符是`ω`的第一个字符`z`。
5. 但`ω`的第一个字符肯定也就是`χ`的第一个字符。
6. 故`ω`一定是`χ`加上`χ`的第一个字符`x`。
7. 这样decoder就知道索引`Z`的值。

最后给出Erlang语言的实现：

    :::erlang
    decompress(E) ->
        Dict = dict:new(),
        if
            length(E) =:= 0 ->
                [];
            true ->
                [Code|EE] = E,
                doDecompress(EE, ?MIN_CODE, [Code], Dict, [Code])
        end.

    doDecompress([], _, _, _, Result) ->
        Result;

    doDecompress([Code|E], Index, Conjecture, Dict, Result) ->
        Value = is_ascii_or_in_dict(Dict, Code),
        if
            Value =:= [] ->
                NewConjecture = Conjecture ++ listify(first_char_of(Conjecture)),
                NewDict = dict:append(Index, NewConjecture, Dict),
                doDecompress(E, Index + 1, listify(NewConjecture), NewDict, Result ++ listify(NewConjecture));
            true ->
                NewDict = dict:append(Index, Conjecture ++ listify(first_char_of(Value)), Dict),
                doDecompress(E, Index + 1, listify(Value), NewDict, Result ++ listify(Value))
        end.

    first_char_of(List) when is_list(List) ->
        if
            length(List) >= 1 ->
                lists:nth(1, List);
            true ->
                []
        end;
    first_char_of(Char) ->
        Char.

    test() ->
        SS = ["",
              "A",
              "ABABABAB",
              "AAAAAAAA",
              "BABAABBAAABBBBAAAAA",
              "TOBEORNOTTOBEORTOBEORNOT",
              "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
              "AABABBBABAABABBBABBABB" ],
        io:format("~p~n", [[length(X) || X <- SS]]),
        EE = [compress(S) || S <- SS],
        io:format("~p~n", [[length(X) || X <- EE]]),
        SS1 = [decompress(E) || E <- EE],
        SS =:= SS1.

上述代码对Unicode字符串进行压缩时就会失败，但我们可以将`MIN_CODE`define得比每个Unicode的数值都大时，就工作正常了。

参考：  
[LZW on Wikipedia](http://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)  
[LZ77 & LZ78](http://en.wikipedia.org/wiki/LZ77_and_LZ78)  
[Run-length Encoding](http://en.wikipedia.org/wiki/Run-length_encoding)  