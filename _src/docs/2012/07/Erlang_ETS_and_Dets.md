ETS is Erlang Term Storage and Dets is Disk Erlang Term Storage.

ETS
------

There are four different kinds of ETS tables. Set, Ordered set, Bag, and Duplicate bag.


- In a `set`, each key can occur only once.
- An `ordered set` has the same property as the set, but it is stored so that the elements can be traversed following the lexicographical order on the keys.
- A `bag` allows multiple entries for the same key, permitting entries such as {"refac torings",4} and {"refactorings",34}. The elements have to be distinct
- A `duplicate bag` allows duplicated elements, as well as duplicated keys.

The implementations of these collections give a constant lookup time for elements, except in the case of ordered sets, where the access time is logarithmic in the size of the collection. An ordered set, where the order is given by the built-in order on the key field, is stored as an AVL balanced binary tree.

Sets, bags, and duplicate bags are stored as hash tables, where the position in the table storing the tuple is determined by the value of a function (called a hash function) map- ping the key of the tuple to the memory location where its contents are stored.


The implementation of ETS tables in the Erlang distribution is very flexible, allowing key fields to be of any type, including complex data structures. Moreover, it is highly optimized, since it forms the foundation for implementing Erlang’s Mnesia database.




    :::erl
    1> TableId = ets:new(test, [set]). %% set can be replaced with ordered_set, bag, duplicate_bag
    16400
    2> ets:insert(TableId, {name, mitnk}).
    true
    3> ets:lookup(TableId, name).
    [{name,whg}]
    4> ets:insert(TableId, {age,16#1d}).
    true
    5> ets:tab2list(TableId).
    [{age,20},{name,mitnk}]
    6> ets:delete(TableId).
    true

Create a named_table:

    :::erl
    1> ets:new(myBag, [bag, named_table]).
    myBag
    2> ets:insert(myBag, {name, mitnk}).
    true

Let play this:

    :::erl
    3> tv:start().


Dets
-------

    :::erl
    1> dets:open_file(food, [{type, bag}, {file, "./food"}]).
    {ok,food}
    2> dets:insert(food, {italy, spaghetti}).
    ok
    3> dets:lookup(food, china).
    []
    4> dets:insert(food, {italy, pizza}).
    ok
    5> dets:insert(food, {sweden, meatballs}).
    ok
    6> NotItalian = ets:fun2ms(fun({Loc, Food}) when Loc /= italy -> Food end).
    [{{'$1','$2'},[{'/=','$1',italy}],['$2']}]
    7> dets:select(food, NotItalian).
    [meatballs]
    8> dets:info(food).
    [{type,bag},
     {keypos,1},
     {size,3},
     {file_size,5536},
     {filename,"./food"}]

