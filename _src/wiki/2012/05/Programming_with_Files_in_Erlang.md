Organization of the Libraries
-------------

The functions for file manipulation are organized into four modules:

- file 
    - This has routines for opening, closing, reading, and writing files; listing directories; and so on. [docs](http://www.erlang.org/doc/man/file.html)

- filename
    - This module has routines that manipulate filenames in a platform- independent manner, so you can run the same code on a number of different operating systems. [docs](http://www.erlang.org/doc/man/filename.html)

- filelib
    - This module is an extension to file, which contains a number of utilities for listing files, checking file types, and so on. Most of these are written using the functions in file. [docs](http://www.erlang.org/doc/man/filelib.html)

- io
    - This module has routines that work on opened files. It contains routines for parsing data in a file and writing formatted data to a file. [docs](http://www.erlang.org/doc/man/io.html)


The Different Ways of Reading a File
----------------

Content of `data.txt`

    {person, "joe", "armstrong",
        [{occupation, programmer},
         {favoriteLanguage, erlang}]}.

    {cat,
        {name, "zorro"},
        {owner, "joe"}}.

**Reading All the Terms in the File**

    :::erl
    1> file:consult("data.txt").
    {ok,[{person,"joe","armstrong",
                 [{occupation,programmer},{favoriteLanguage,erlang}]},
         {cat,{name,"zorro"},{owner,"joe"}}]}

**Reading the Terms in the File One at a Time**

    :::erl
    1> {ok, S} = file:open("data.txt", read).
    {ok,<0.33.0>}
    2> io:read(S, '').
    {ok,{person,"joe","armstrong",
                [{occupation,programmer},{favoriteLanguage,erlang}]}}
    3> io:read(S, '').
    {ok,{cat,{name,"zorro"},{owner,"joe"}}}
    4> io:read(S, '').
    eof
    5> io:read(S, '').
    eof
    6> file:close(S).
    ok
    7> io:read(S, '').
    {error,terminated}

**Which lib**

    1> code:which(file).
    "/usr/local/lib/erlang/lib/kernel-2.15/ebin/file.beam"

**Reading the Lines in a File One at a Time**

    :::erl
    1> {ok, S} = file:open("data.txt", read).
    {ok,<0.33.0>}
    2> io:get_line(S, '').
    "{person, \"joe\", \"armstrong\",\n"
    3> io:get_line(S, '').
    "    [{occupation, programmer},\n"
    4> io:get_line(S, '').
    "     {favoriteLanguage, erlang}]}.\n"
    5> io:get_line(S, '').
    "\n"
    6> io:get_line(S, '').
    "{cat,\n"
    7> io:get_line(S, '').
    "    {name, \"zorro\"},\n"
    8> io:get_line(S, '').
    "    {owner, \"joe\"}}.\n"
    9> io:get_line(S, '').
    "\n"
    10> io:get_line(S, '').
    eof
    11> file:close(S).    
    ok


**Reading the Entire File into a Binary**

    :::erl
    1> file:read_file("data.txt").
    {ok,<<"{person, \"joe\", \"armstrong\",\n    [{occupation, programmer},\n     {favoriteLanguage, erlang}]}.\n\n{cat,\n    {n"...>>}

**Reading a File with Random Access**

If the file we want to read is very large or if it contains binary data in some externally defined format, then we can open the file in raw mode and read any portion of it using file:pread.

    :::erl
    1> {ok, S} = file:open("data.txt", [read, binary, raw]).
    {ok,{file_descriptor,prim_file,{#Port<0.574>,11}}}
    2> file:pread(S, 22, 46).
    {ok,<<"rong\",\n        [{occupation, programmer},\n    ">>}
    3> file:pread(S, 1, 10).
    {ok,<<"person, \"j">>}
    4> file:pread(S, 2, 10).
    {ok,<<"erson, \"jo">>}
    5> file:close(S).
    ok

The Different Ways of Writing to a File
------------------

**Write a List of Terms to a File**

    :::erl
    1> {ok, S} = file:open("output.txt", write).
    {ok,<0.33.0>}
    2> L = [{name, tom}, {age, 2}].
    [{name,tom},{age,2}]
    3> lists:foreach(fun(X) -> io:format(S, "~p~n", [X]) end, L).
    ok

**Writing to a Random-Access File**

    :::erl
    1> {ok, S} = file:open("...", [raw,write,binary]) {ok, ...}
    2> file:pwrite(S, 10, <<"new">>)
    ok

Finding Information About a File
-----------------

    :::erl
    2> file:read_file_info("output.txt").
    {ok,{file_info,19,regular,read_write,
               {{2012,5,19},{18,5,2}},
               {{2012,5,19},{18,4,56}},
               {{2012,5,19},{18,4,56}},
               33188,1,234881026,0,1740577,502,20}}
