这是Stackoverflow上一个贴子[1]的翻译，原文对yield关键字解释得很是明了，就翻译过来了。

要理解yield关键字，你必须先理解generator是什么；而理解generator我们最好先理解iterable是什么。

Iterables
---------

像list这样的，可以一个元素一个元素的读，这个过程就叫iteration（迭代）：

    :::python
    >>> mylist = [1, 2, 3]
    >>> for i in mylist:
    ...    print(i)
    1
    2
    3

mylist就是一个iterable。下面代码用list的语法创建了一个list，也即iterable：

    :::python
    >>> mylist = [x*x for x in range(3)]
    >>> for i in mylist:
    ...    print(i)
    0
    1
    4

所有你可以对之使用 `for ... in ...` 的东西就是一个iterable: 比如 list, string, files 等。因为我们想读多少就读多少，所以iterable非常方便。但是这样我们是将所有的值都放入内存中了，这可能不是我们想要的。

Generators
---------

Generators（生成器）也是iterables，但是你只能读取它们一次。因为它们没有将值放入内存，每一次迭代取到的值都是即时生成的：

    :::python
    >>> mygenerator = (x*x for x in range(3))
    >>> for i in mygenerator:
    ...    print(i)
    0
    1
    4

这里我们用 `( )` 代替了 `[ ]`，效果看似是一样的。但这里你不能第二次调用 `for i in mygenerator`，因为generators仅可被使用一次：它计算并返回了0，然后就扔掉了它，然后再生成1，再扔掉，最后生成4。

Yield
-----

`yield` 是一个很像 `return` 的一个关键字，只不过它使得函数返回一个generator。

    :::python
    >>> def createGenerator():
    ...    mylist = range(3)
    ...    for i in mylist:
    ...        yield i*i
    ...
    >>> mygenerator = createGenerator() # create a generator
    >>> print(mygenerator) # mygenerator is an object!
    <generator object createGenerator at 0xb7555c34>
    >>> for i in mygenerator:
    ...     print(i)
    0
    1
    4

（个人觉得原作者这个例子举得不是很好，后面有说明）

这个例子貌似没做什么特别有用的事情，但如果你想让一个函数返回包含很多很多元素的列表时且只需要读取一次时，它就变得有用了。

对于 `yield` ，你必须了解一点：**当你调用函数时，函数的主体代码并没有执行**，只是返回了一个generator对象。这多少有点诡异。

之后，当你每次在 `for` 中使用这个generator时，代码才会执行。

现在说难点（也是重点）：

第一次你的函数主体代码被执行时，它会比函数开头一直执行到 `yield` 处，并返回（第）一个值。之后，每次这个generator被多调用一次，就会多计算一个值并返回它（注意这时并不会从头执行函数，而只是执行loop部分），直到没有值可被返回。

More
----

以下是我加的，没有在原文里。

在代码内部，当用 `for` 来使用 generator 时，其实是不断调用 generator 的 `next()` 方法，直到遇到代表generator已经为空，没有更多值可返回的 `StopIteration` 异常为止。

    :::python
    In [1]: def make_times(n):
       ...:     i = 0
       ...:     while i < n:
       ...:         yield i
       ...:         i += 1
       ...:

    In [2]: gene = make_times(3)

    In [3]: gene.next()
    Out[3]: 0

    In [4]: gene.next()
    Out[4]: 1

    In [5]: gene.next()
    Out[5]: 2

    In [6]: gene.next()
    ------------------------------------------------
    StopIteration        Traceback (most recent call last)
    <ipython-input-6-58dad61ab61e> in <module>()
    ----> 1 gene.next()

    StopIteration:

注意这里我们没有像原文一样用 `range()`，因为那样并不会用到 generator 的优点：
不将“整个列表”放到内存里。用 `for i in range(1000000)` 时，已经在内存里创建了
一个拥有100万个元素的列表。Python中的`xrange()`之所以被推荐就是用了generator的
技术。

[1] [The Python yield keyword explained](http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained)