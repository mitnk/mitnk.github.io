Lua语言表达式与控制语句
=======================

Lua（英語發音：/ˈluːə/）程式語言是一個簡潔、輕量、可延伸的手稿語言，
是葡萄牙語中「Lua」（月亮）的意思。[1]

继Lua的基本类型[2]，现在开始表达式(Expressions)和控制语句(Statements) [3]的笔记。

表达式
------

**代数操作符**

    :::lua
    > = 3 ^ 4
    81
    > = -7 % 3
    2

对于一个数字`x`, `x % 1`是它的小数部分 -- `a % b == a - math.floor(a / b) * b`


**比较操作**

除了不等于不Lua里为 `~=` 外，其余操作符都与C语言里相同。


**逻辑操作符**

    :::lua
    > = 4 or 5  --> 4
    > = 4 and 5 --> 5
    > = false and 13 --> false
    > = false or 13 --> 13
    > = not false --> true
    > = not nil --> true
    > = not 0 --> false


**长度计算**

    :::lua
    > = #"Hello" --> 5
    > = #{1, 3, 5, 7} --> 4


**Lua操作符优先级列表**

    :::lua
    ^
    not # - (unary) */%
    +-
    ..
    < > <= >= ~= == and
    or


控制语句（statements）
-------------------

**赋值**

a, b, c = 3, 5  -- a = 3; b = 5; c = nil

**局部变量与代码块**

    :::lua
    x = 10
    local i = 1  -- local to the chunk

    while i <= x do
        local x = i*2  -- local to the while body
        print(x)  --> 2, 4, 6, 8, ...
        i = i + 1
    end

    if i > 20 then
        local x  -- local to the "then" body
        x = 20
        print(x + 2)  -- (would print 22 if test succeeded)
    else
        print(x)  --> 10  (the global one)
    end

    print(x)  --> 10  (the global one)

注意这个例子不能在解释器交互模式下工作，因为在交互模式下，每一行都是一个Chunk。
但你可以用 `do ... end` 来做试验。


**if语句**

    :::lua
    if a < 0 then a = 0 end

    if a < b then return a else return b end

    if op == "+" then
        r = a + b
    elseif op == "-" then
        r = a - b
    elseif op == "*" then
        r = a * b
    else
        error("invalid operation")
    end


**while语句**

    :::lua
    a = {1, 3, 5, 7}
    local i = 1
    while a[i] do
        print(a[i])
        i = i + 1
    end


**for语句**

for语句有两种形式：

1) Numberic for

    :::lua
    for i = 1, 3 do
        print(i)
    end

    for i = 3, 1, -1 do
        print(i)
    end

    for i = 1, 2.5 do
        print(i)
    end

    -- Output are:
    -- 1
    -- 2
    -- 3
    -- 3
    -- 2
    -- 1
    -- 1
    -- 2

2) Generic for

    :::lua
    child = {name='Tommy', age=7}
    for k, v in pairs(child) do
        print(k, v)  -- there will be a <Tab> between k and v.
    end
    -- Output:
    -- age    7
    -- name   Tommy

    days = {'a', 'b', 'c'}
    for k, v in pairs(days) do
        print(k, v)
    end
    -- Output:
    -- 1    a
    -- 2    b
    -- 3    c


**Repeat语句**

    :::lua
    -- print the first non-empty input line
    repeat
        line = io.read()
    until line ~= ""
    print(line)


[0] [Book: Programming in Lua](http://www.amazon.com/Programming-Lua-Roberto-Ierusalimschy/dp/859037985X)  
[1] [http://zh.wikipedia.org/wiki/Lua](http://zh.wikipedia.org/wiki/Lua)  
[2] [Lua语言基本类型](/2014/11/lua_tutor_basic_types/)  
[3] [云风的翻译为语句段](http://www.codingnow.com/2000/download/lua_manual.html)  
