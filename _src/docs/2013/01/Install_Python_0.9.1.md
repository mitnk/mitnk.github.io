Python官网有一个0.9.1的古老版本[1]，这个源码包大小只有380K，而且可以正常编译安装（在Mac 10.8、Arch Linux上测试通过）：

    wget http://www.python.org/download/releases/early/Python-0.9.1.tar.gz
    tar xf Python-0.9.1.tar.gz
    cd python-0.9.1/src/
    make
    cp -v python /usr/local/bin/python0.9

当然了功能非常有限：

    :::python
    $ python0.9 
    >>> import os
    Unhandled exception: undefined name: os
    Stack backtrace (innermost last):
      File "<stdin>", line 1
    >>> [x for x in range(7)]
    Parsing error: file <stdin>, line 1:
    [x for x in range(7)]
          ^
    Unhandled exception: run-time error: syntax error
    >>> [1, 3] + [2, 4]
    [1, 3, 2, 4]
    >>> import math
    >>> dir(math)
    ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'e', 'exp', 'fabs', 'floor', 'log', 'log10', 'pi', 'pow', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']

这么小的代码量（只有8k行Python代码，和3w行C代码），非常适合读来了解Python语言内部实现。（虽然具体实现与现在的2.x/3.x相比，可能已经完全不同了）

[1] <http://www.python.org/download/releases/early/>