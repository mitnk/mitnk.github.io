Singleton模式是一个很有用，但被[很多人](http://blogs.msdn.com/b/scottdensmore/archive/2004/05/25/140827.aspx) [诟病](http://steve.yegge.googlepages.com/singleton-considered-stupid)的设计模式。这里不讨论它的缺点，
而仅仅讨论一下如何在 Python 中实现 Singleton 模式。

<h3>module加function</h3>

Staale认为仅仅用module加function就可以达到目的了。这个方法[在SO上](http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python)得到了
大多数人的支持。

in `a.py`:

    :::python
    get_foo():
        print 'getting foo ...'
        return 'bar'
    foo = get_foo()

in `others.py`:

    :::python
    import a
    print a.foo

<h3>我就要经典的Singleton模式！</h3>

好吧，好吧。经典的来了。

    :::python
    class Singleton(type):
        def __init__(cls, name, bases, dict):
            super(Singleton, cls).__init__(name, bases, dict)
            cls.instance = None

        def __call__(cls, *args, **kwargs):
            if cls.instance is None:
                cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls.instance

    class A(object):
        __metaclass__ = Singleton

    if __name__ == '__main__':
        a1 = A()
        a2 = A()
        print id(a1) == id(a2)

这个方法有一个小问题，它不能通过 `deepcopy` 的测试：

    :::python
    from copy import deepcopy
    a3 = A()
    a4 = deepcopy(a3)
    print id(a3) == id(a4)


<h3>经典版本2</h3>

也可以通过重写 `__new__` 方法来实现相同的目的。并且没有 `deepcopy` 的问题

    :::python
    class A(object):
        _instance = None
        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(A, cls).__new__(cls, *args, **kwargs)
            return cls._instance


<h3>Borg模式</h3>

Singleton模式强调的是一个类只能实例化一次，但我们目的只是让实例的状态
唯一就行了，不用管它被实例化多少次。 [Google员工、Python大牛Alex Martelli写了一个Borg设计模式](http://code.activestate.com/recipes/66531/)
被很多人认为可以在Python中替代Singleton模式。

    :::python
    class Borg(object):
        __shared_state = {}
        def __init__(self):
            self.__dict__ = self.__shared_state

    if __name__ == '__main__':
        b1 = Borg()
        b2 = Borg()
        b1.name = 'hi'
        print b1.name, b2.name

        b2.age = 20
        b3 = Borg()
        print b1.age, b2.age, b3.age

Result:

    :::bash
    hi hi
    20 20 20

<h3>选择哪个？</h3>

我觉得用哪个问题都不大，看个人口味了。Django[用到了Borg模式](https://github.com/django/django/blob/b8244c654c85034bd4209a93a7802eb306c32e2b/django/db/models/loading.py#L23)。