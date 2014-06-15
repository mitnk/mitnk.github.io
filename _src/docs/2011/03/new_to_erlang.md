之前从<a href="http://www.cnblogs.com/lidaobing/">李道兵</a>、<a href="http://blog.codingnow.com/">云风</a>、<a href="http://www.douban.com/people/hongqn/">洪强宁</a>那里听到过Erlang语言  
对其没有任何概念，除了知道它是一门编程语言  
春节几天假里花了点时间学习了一下  
在这里分享下。。。  

Ubuntu系统本身就自带了一个Erlang解释器  
在Terminal下执行erl即可  
（如果没有就用sudo apt-get install erlang安装一下）  

让我们执行第一个Erlang语句吧：  

    :::erl
    $ erl
    1> 2 + 17 / 8.
    4.125

（不要看漏后面的点号哦。。。）  

Erlang能执行单句的特性真是太棒了  
Python程序员常以Python可以方便地用作计算器而洋洋自得  
现在要知道Erlang也是可以的：）  

再看下面一段代码：  

    :::erl
    2> X = 123456789.
    123456789
    3> X * X * X * X.
    232305722798259244150093798251441
    4> X = 123.
    ** exception error: no match of right hand side value 123


Erlang和Python一样本身就支持很大很大的数字！ 很强吧！  

首先这里的X并不是变量  
（至少不像C、Jave、Python语言里的变量）  
因为他不是变量所以你不能更改X的值  
（如X=123.这个操作）  
然后，这里的=号也不是赋值操作符  
注意上面的Error信息，它说两边值不匹配  
也就是Erlang里的=号为匹配操作符  

为方便描述，我们还是叫这里的X为变量  
只不过是只能被“赋值”一次（通过匹配操作符）  

在C语言中我们有时需要定义一个常量  
我们通常会用宏来定义，如：  

    :::c
    #define NULL 0


而在Erlang里我们不用这么麻烦  
直接说null就好了（小写开头的名称）  

    :::erl
    1> null.
    null


也就是说Erlang里不能用小写字母开头的名称来作变量名  
比如在前例中不能有x = 123456789. 来操作  

说过一些基本的东东后，再来瞧瞧Erlang的函数吧  
（Erlang本身是一门函数式编程语言）  

下面是一个计算阶乘的函数  
请将这些代码存为 fact.erl 文件  

    :::erlang
    -module(fact).
    -export([fact/1]).
    fact(0) -> 1;
    fact(N) -> fact(N - 1) * N.


然后是编译执行的过程：  

    :::erl
    $ erlc fact.erl
    $ erl
    1> fact:fact(7).
    5040

用erlc编译后，会在同文件夹下生成一个beam文件  

再写一个有关list数据结构的函数  
在写之前先用代码演示下list的一个有意思的语法  

    :::erl
    1> L = [1, 3, 5, 7].
    [1,3,5,7]
    2> L.
    [1,3,5,7]
    3> [H|T] = L.
    [1,3,5,7]
    4> H.
    1
    5> T.
    [3,5,7]
    6> [H1|T1] = T.
    [3,5,7]
    7> H1.
    3
    8> T1.
    [5,7]
    9> [H2|T2] = [7].
    [7]
    10> H2.
    7
    11> T2.
    []


我想读了这段代码就会明白list的head和tail语法了  
那么下面写个sum函数以计算一个list所有元素之和  

    :::erlang
    -module(utils).
    -export([sum/1]).
    sum([]) -> 0;
    sum([H|T]) -> H + sum(T).


将上面代码存为utils.erl并编译执行：  

    :::erl
    $ erlc utils.erl
    $ erl
    1> L = [1, 2, 3, 4, 5].
    [1,2,3,4,5]
    2> utils:sum(L).
    15


读到这里应该会对Erlang有个初步概念了  
当然本篇只提到了顺序编程（Sequential Programming）  
而Erlang擅长的是并行编程（也是它的设计初衷）  
以后再写罢。  
