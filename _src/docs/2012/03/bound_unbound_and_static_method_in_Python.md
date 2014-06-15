先看下面一段代码

    :::python
    class A:
        def foo(self):
            pass
    a = A()
    print A.foo
    print a.foo

输出

    <unbound method A.foo>
    <bound method A.foo of <__main__.A instance at 0x10b06a560>>


这里的关键字是 unbound 和 bound。在[一个 Python 2.3.4 的文档](http://docs.python.org/release/2.3.4/lib/typesmethods.html)中，它们的定义是这样的

<blockquote>
<p>
Methods are functions that are called using the attribute notation. There are two flavors: built-in methods (such as append() on lists) and class instance methods. 
</p>
<p>...</p>
<p>
Class instance methods are either bound or unbound, referring to whether the method was accessed through an instance or a class, respectively. 
</p>
<p>...</p>
</blockquote>

在 ptyhon mail list 中[Kalle Svensson对 bound / unbound methods 的解释](http://mail.python.org/pipermail/tutor/2001-November/009887.html)简明易懂：

--------------

Consider a function and a method:

    def f(x):
        print x

    class C:
        def m(self, x):
            print x

The function takes one argument and prints it, so does the method, if used on
an instance:

    >>> c = C()
    >>> f(1)
    1
    >>> c.m(1)
    1

This means the first method argument, self, appeared from nowhere.  This is
because the method is bound to the instance c.  When a method is not bound to
any instance, you have to supply all arguments yourself, like:

    >>> C.m(c, 1)
    1

This also means that c.m and C.m are not the same thing.  They're *almost* the same, but c.m is bound to the instance c, and C.m is unbound.

-----------

而 Stackoverflow 上 [Armin Ronacher 给出了更加深入的解释](http://stackoverflow.com/a/114289/665869)，非常值得一读

以下为全文引用：

Methods in Python are a very, very simple thing once you understood the basics of the descriptor system. Imagine the following class:

    :::python
    class C(object):
        def foo(self):
            pass

Now let's have a look at that class in the shell:

    :::python
    >>> C.foo
    <unbound method C.foo>
    >>> C.__dict__['foo']
    <function foo at 0x17d05b0>

As you can see if you access the foo attribute on the class you get back an unbound method, however inside the class storage (the dict) there is a function. Why's that? The reason for this is that the class of your class implements a __getattribute__ that resolves descriptors. Sounds complex, but is not. C.foo is roughly equivalent to this code in that special case:

    :::python
    >>> C.__dict__['foo'].__get__(None, C)
    <unbound method C.foo>

That's because functions have a __get__ method which makes them descriptors. If you have an instance of a class it's nearly the same, just that None is the class instance:

    :::python
    >>> c = C()
    >>> C.__dict__['foo'].__get__(c, C)
    <bound method C.foo of <__main__.C object at 0x17bd4d0>>

Now why does Python do that? Because the method object binds the first parameter of a function to the instance of the class. That's where self comes from. Now sometimes you don't want your class to make a function a method, that's where staticmethod comes into play:

    :::python
    class C(object):
        @staticmethod
        def foo():
            pass

The staticmethod decorator wraps your class and implements a dummy __get__ that returns the wrapped function as function and not as a method:

    :::python
    >>> C.__dict__['foo'].__get__(None, C)
    <function foo at 0x17d0c30>

Hope that explains it.

=== End of Quote ===