Python Decorators
=================

## 1. The Basics

What you have to know about Python decorators is to understand the following
code line by line. Note the use of `functools.wraps`.

    :::python
    from functools import wraps
    import time

    def timeit(func):
        def wrapper(*args, **kwargs):
            print('starting {} args: {} kwargs: {}'.format(func, args, kwargs))
            t = time.time()
            result = func(*args, **kwargs)
            print('result: {} timed: {:.4f}s'.format(result, time.time() - t))
            return result
        return wrapper

    def timeit2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('starting {} args: {} kwargs: {}'.format(func, args, kwargs))
            t = time.time()
            result = func(*args, **kwargs)
            print('result: {} timed: {:.4f}s'.format(result, time.time() - t))
            return result
        return wrapper

    @timeit
    def add(a, b):
        """Add two numbers"""
        time.sleep(0.111)
        return a + b

    @timeit2
    def multiple(a, b=81):
        """Multiple two numbers"""
        time.sleep(0.123)
        return a * b

    add(23, 89)
    multiple(23)

    print(add.__name__)
    print(add.__doc__)
    print(multiple.__name__)
    print(multiple.__doc__)

The outputs:

    :::
    starting <function add at 0x10150b8c8> args: (23, 89) kwargs: {}
    result: 112 timed: 0.1147s
    starting <function multiple at 0x101578268> args: (23,) kwargs: {}
    result: 1863 timed: 0.1245s
    wrapper
    None
    multiple
    Multiple two numbers

## 2. Class-based Decorators

    :::python
    import time

    class timeit:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print('starting func call {}'.format(self.func))
            t = time.time()
            result = self.func(*args, **kwargs)
            print('timed {:.4f}'.format(time.time() - t))
            return result

    @timeit
    def add(a, b):
        return a + b

    @timeit
    def multiple(a, b):
        return a * b

    print(add(2, 3))
    print(multiple(2, 3))

## 3. Decorators on Class

Decorators can also work on class, though it is sort of weird.

    :::python
    from functools import wraps
    import time

    def timeit(func, *args, **kwargs):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('starting {}'.format(func))
            t = time.time()
            result = func(*args, **kwargs)
            print('result: {} timed: {:.4f}s'.format(result, time.time() - t))
            return result
        return wrapper

    def time_all_methods(klass):
        class NewClass(object):
            def __init__(self, *args, **kwargs):
                self.origin_instance = klass(*args, **kwargs)

            def __getattribute__(self, name):
                try:
                    x = super(NewClass, self).__getattribute__(name)
                except AttributeError:
                    pass
                else:
                    return x

                obj = self.origin_instance.__getattribute__(name)
                if hasattr(obj, '__call__'):
                    return timeit(obj)
                return obj
        return NewClass

    @time_all_methods
    class Calc(object):
        """The calculator on two numbers"""

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def add(self):
            """Add them"""
            return self.a + self.b

        def multiple(self):
            """Multiple them"""
            return self.a * self.b


    c = Calc(3, 7)
    c.add()
    c.multiple()
    print(c)
    print(c.__doc__)

The outputs:

    :::
    starting <bound method Calc.add of <__main__.Calc object at 0x101801990>>
    result: 10 timed: 0.0000s
    starting <bound method Calc.multiple of <__main__.Calc object at 0x101801990>>
    result: 21 timed: 0.0000s
    <__main__.NewClass object at 0x101801950>
    None

