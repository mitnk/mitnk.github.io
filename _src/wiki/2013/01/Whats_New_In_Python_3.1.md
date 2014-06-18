PEPs
------

- Added `OrderedDict` in collections module- Built-in `format()`: format(1234567.89, ',.2f') => '1,234,567.89'


Other Language Changes
----------------------------

- Directories and zip archives containing a `__main__.py` file can be executed by passing their names to the interpreter.
- `bit_length()`: `n = 2**123-1; n.bit_length()` => `123`
- `'Sir {} of {}'.format('Foo', 'Bar')'`
- string.maketrans() was replaced by `bytes.maketrans()`
- with statement: `with open('a.txt') as infile, open('b.txt') as outfile:`
- round(x, n) now returns integer if x is an integer
- repr(1.1) now is '1.1', previously, it's '1.1000000000000001'

New, Improved, and Deprecated Modules
-----------------------------------------------

- Added collections.`Counter` class to support counting of unique items in a sequence.
- Added a new module `tkinter.ttk` for access to the Tk themed widget set.
- The `gzip.GzipFile` and `bz2.BZ2File` classes now support the context manager protocol (the `with` .. `as` statement)
- The `decimal` module now supports methods for creating a decimal from `float`: `Decimal.from_float(1.1)`
- The `itertools` module grew two new functions. The `itertools.combinations_with_replacement()` for generating combinatorics including permutations and Cartesian products. The `itertools.compress()` mimics namesake from APL.
- Added the `rename` argument for `collections.namedtuple()`
- The `re.sub(), re.subn()` and `re.split()` now accept a flags parameter.
- The `logging` module now implements a simple `logging.NullHandler` class.
- The `runny` which supports the `-m` switch now supports the execution the `__main__` when a package name is supplied.
- The `pdb` now support `zipimport` codes
- `functools.partial` objects can now be pickled.
- The `unit test` module now supports skipping individual tests or classes of tests. And it supports marking a test as a expected failure. `@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")` and `@unittest.expectedFailure`
- Also, tests for exceptions have been builtout to use `with` statement. More assertion methods were added like `assertTupleEqual(), assertSequenceEqual()`, etc.
- The `io` module has three new constants for the `seek()` method. `SEEK_SET`, etc
- A new module `importlib` was added. It provides a complete, portable, pure Python reference implementation of the `import` and `__import__()`.


Optimizations
---------------

Major performance enhancements have been added:

- The I/O library has been entirely rewritten in C and is 2 to 20 times faster than it in Python 3.0 (The python version is still available at `_pyio` for experimentation purposes.
- Added a heuristic so that tuples and dicts containing only untrackable objects are not tracked by the garbage collector.
- The decoding of UTF-8, UTF-16, and LATIN-1 is now two to four times faster.
- The `json` module now has a C extension to substantially improve its performance.
- Unpickling now interns the attribute names of pickled objects. This save memory and allow pickles to be smaller.