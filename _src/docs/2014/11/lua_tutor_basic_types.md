lua编程语言基本类型
===================

最近开始学习流行脚本语言中最简单的[lua语言](http://www.lua.org/about.html)。
而这个部落格已经长满野草了， 故在这里新添篇笔记吧（而不是在Evernote里：）。

安装
----

我是用brew把lua (v5.2.3)安装到mac上的

    $ brew install lua

lua的Say Hi

    :::lua
    $ lua
    > print("Hello World")
    Hello World
    > os.exit()

通过文件执行lua是这样的

    $ lua hello.lua

表达式
------

lua中的回车符和空格一样，对程序解析没有影响

    :::lua
    > a = 3 b = a * 2 -- ugly, but valid
    > print(b)
    6

import文件
----------

如下面一个文件 hello.lua

    :::lua
    function hi()
        print('hi')
    end

将函数 `hi()` 引入到上下文中有三种方式

1) 启动lua时用 `-i` 执行此文件

    :::lua
    $ lua -i hello.lua
    > hi()
    hi

2) 用 dofile 执行此文件

    :::lua
    > dofile('hello.lua')
    > hi()
    hi

3) 以 require lib 的方式引入

    :::lua
    $ lua -l hello
    > hi()
    hi


注释
----

    :::lua
    a = 1  -- single line comment
    --[[
        you can put multiple lines of comments
        here.
    ]]
    b = 2
    --[==[
        you can put any number of = between []
        if there are ]] inside comment content
    ]==]
    c = 3


基本类型
--------

lua中共有八种类型

- nil
- boolean
- number
- string
- userdata
- function
- thread
- table

nil 和 boolean
--------------

没有定义过的变量的值为 nil

    :::lua
    > = type(foo)
    nil
    > = foo
    nil
    > = foo == nil
    true
    > foo = 1
    > = foo
    1

将一个变量设为nil会使被删除，其内存最终会被GC回收。

boolean类型里只有两个值: `true` 和 `false`. 在bool判定中只有 `false` 和 `nil`为假，
其余都会为真（包括0或空table）

    :::lua
    > a = false
    > if a then
    >>  print('hi')
    >> end
    > a = 0
    > if a then
    >>  print('hi')
    >> end
    hi


number
------

lua没有专门的整数integer类型，所以 2 和 2.5 的类型是一样的

    > = type(2)
    number
    > = type(2.5)
    number

string
------

    :::lua
    > a = 'hi'
    > = a .. ' there'
    hi there
    > = '\097'
    a
    > = '\x61\x62\x63'
    abc
    > = tonumber('2') + 3
    5
    > 10 + '234'  -- lua automatically convert string to number if necessary
    244


table
-----

lua中的table同时表达了列表和哈希表两种数据类型

    :::lua
    a = {}  -- create an empty table
    for i = 1, 100 do a[i] = i * i end
    print(a[5])  --> 25

    print(#a)  --> 100
    a[101] = 3
    print(#a)  --> 101
    a[500] = 3
    print(#a)  --> still be 101, because of gaps between 101 and 500

    b = a
    b[5] = 26
    print(a[5])  --> 26  -- because a and b are identical

    a = {title='Writer'}
    print(a['title'])  --> Writer
    a['name'] = 'Hugo'
    print(a['name'])  --> Hugo
    print(a.name)  --> Hugo
    a.age = 7
    print(a['age'])  --> 7


function
--------

lua中的函数和普通变量一样，和Python一样可以被传来传去的，没什么可说的。


这就是lua语言中的所有类型了。
