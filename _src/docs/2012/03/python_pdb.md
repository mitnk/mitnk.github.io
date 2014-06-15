<h3>pdb常用的启动方式</h3>

a) 通过 pdb.run 方法：

    :::python
    >>> import pdb
    >>> import mymodule
    >>> pdb.run('mymodule.test()')

b) 命令行参数方式

    python -m pdb myscript.py


c) 最常用的是将下面一行插入到欲Debug的代码特定位置：

    :::python
    import pdb; pdb.set_trace()

然后执行代码。

<h3>(Pdb)模式下的常用命令</h3>

q  
退出debug

h 
即help，打印所有可以命令

h w   
打印命令 `w` 的含意

n  
执行当前行直到到达下一行或直到它返回

s  
执行当前行，一有可能就停止（比如当前行有一个函数调用）。它和n(next)的区别是当前行中有函数调用时s(step)会停止当前行的执行而去调用那个函数，而n不会停止，直到计算完成这一行（到达下一行）。

b(reak) [[filename:]lineno | function[, condition]]  
设置断点，可以是行号或函数。如 `b 10`, `b foo`, `b foo,n == 5`，最后在函数`foo()`入口处设置一个断点，但仅当n的值是5时才有效。当`b`命令无参数时，打印所有断点。

tb(reak) [[filename:]lineno | function[, condition]]  
临时断点，只hit一次。

disable [bpnumber [bpnumber ...]]  
使指点行的断点（们）失效

enable [bpnumber [bpnumber ...]]  
使指定行上的断点（们）有效

c  
继续执行程序，直到遇到下一个断点

w  
即where，打印当前执行点的位置

l [first, [,last]]  
输出当前行附近的源码

p expression  
执行一个表达式当打印其值。

a(rgs)  
打印当前函数的参数及其值

<直接回车>  
重复执行上次的命令

并遇到pdb不认识的命令时，会将它当成python表达式执行。如果你想执行的表达时，最前面加上 `!` 字符，比如 `!n == 5`

多个debug命令可以写在一行上，中间用两个分号分隔，如 `s;;s`。
