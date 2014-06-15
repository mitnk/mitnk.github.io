Common Stumbling Blocks
-------------------------

- print is a function now
- Views and iterators instead of lists
- Ordering Comparisons
- Integers
- Text Vs. Data: The type used to hold text is str, the type used to hold data is bytes

Syntax Changes
--------------

**New Syntax**

- `__annotations__`
- def a(*args, via)
- new reserved word: nonlocal
- (a, *rest, b) = range(10)
- {k: v for k, v in stuff}
- Set literals: {1, 3, 5, 7}
- 0o72
- 0b1010111
- b'this is a bytes type'

**Changed Syntax**

- raise [expr [from expr]]
- `except exc, e` to `except exc as e`
- class C(metaclass=M)
- [1, 3, 5, …, 99]

**Removed Syntax**

- backticks (use repr() instead)
- <> (use != )
- Removed the L or l in long numbers: 1000000000000000L
- Removed U or u for the leading strings: u'abcd'
- The from module import * only allowed in module level, no longer inside functions
- Classic classes are gone

**Changes already Present in Python 2.6**

- bin, oct, hex: bin(173) => '0b10101101'
- class decorators

Library Changes
-------------------

- md5 replaced by hashlib
- use pickle instead of cPickle (python will try import cPickle first)
- related modules have been grouped into packages: e.g. urllib (urllib, urllib2, urlparse, robot parse)
- PEP 3101: the % string formatting operator will removed

Changes to Exceptions
-------------------------

- All exceptions must be derived from BaseException
- ETC

Miscellaneous Other Changes
---------------------------------

- The concept of "unbound methods" has been removed from the language
- Removed `__getslice__`, a[i:j] now is `a.__getitem__(slice(i, j))`
- next() has been renamed to `__next__()`
- Removed `__members__` and `__methods__`
- `__nonzero__()` is now `__bool__()`

Builtins
----------

- New super(). Now we can invoke super() without arguments
- raw_input was renamed to input()
- next() is added
- round(2.5) returns 2
- Removed callable(). Use is instance(f, collections.Callable)
- Removed reduce(). Use functors.reduce()
- Removed reload(). Use imp.reload()


Build and C API Changes
---------------------------

- Support for several platforms was dropped.
- New Buffer API
- etc


Performance
---------------

The pystone benchmark result of Python 3.0 is 10% slower than Python 2.5. Most likely the biggest cause is the removal of small integers.

Porting To Python 3.0
------------------------

0. Start with excellent test coverage
1. Port to Python 2.6
2. Turn on the -3 command line switch
3. Run the 2to3 tool over your source code tree

It is not recommended to try to write source code that runs unchanged under both Python 2.6 and 3.0
