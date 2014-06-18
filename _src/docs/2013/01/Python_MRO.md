Python 2.X版本里类分类两种，经典类和新类。它们有什么区别呢？

其中之一是类的MRO (Method Resolution Order)不同。MRO是什么呢？

阅读以下程序，

    :::python
    class D: # Note: Old-style
        def f(self):
            return "D.f()"

    class C(D):
        def f(self):
            return "C.f()"

    class B(D): pass
    class A(B, C): pass

    a = A()
    print a.f()

请问程序的输出是什么？

如果将上面程序中第一行改为：`class D(object):` 后输出又是什么呢？

经典类（旧类）版程序输入为：`D.f()`  
而新类版本程序输出为： `C.f()`

MRO就是子类的继承图谱、继承顺序。也就是说经典类和新类的MRO使用的是不同的算法。
从上面的程序可以看出新类的MRO算法再“人性”一点。

新类MRO用的是C3算法[1]很有意思，推荐一读。

[1] [The Python 2.3 Method Resolution Order](http://www.python.org/download/releases/2.3/mro/)  
[2] Reference: [Python’s new classes vs old classes](http://unspecified.wordpress.com/2010/11/18/pythons-new-classes-vs-old-classes/)
