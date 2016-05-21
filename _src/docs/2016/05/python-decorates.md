Python Decorators
=================

## The Basics

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

    :::bash
    starting <function add at 0x10150b8c8> args: (23, 89) kwargs: {}
    result: 112 timed: 0.1147s
    starting <function multiple at 0x101578268> args: (23,) kwargs: {}
    result: 1863 timed: 0.1245s
    wrapper
    None
    multiple
    Multiple two numbers


