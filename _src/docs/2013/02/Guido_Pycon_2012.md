Guido gave a great talk [1] on Pycon 2012, on the follow trolls:

- Language Comparisons
    - "Python sucks, Ruby rules"
- Python 3
    - "When will you admit Python 3 is a mistake?"
- PyPy
    - "Since PyPy is so much faster than CPython, why not just abandon CPython"
- Dynamic Typing
    - "I don't want my app to fail with an AttributeError after running for 4 hours"
- Speed
    - "Python is too slow for real work"
    - "Why don't you write a compiler"
- The GIL
    - "Python is useless because of the GIL"
    - "You cannot use it on a multi-core computer"
    - "Why don't you support real threads?"
- Async I/O and Concurrency
    - "When will you integrate Stackless?"
    - "When will you add a proper event loop?"
    - "Why don't you add gevent to the stdlib?"
    - "Why don't you add channels / message passing / actors / Erlang-style processors /
       {my favorite synchronization abstraction}?"
- The Browser
    - "Please make Python work in the browser. It would solve all the world's problem."
- Mobile
    - "You work for Google [1]. Why didn't you make Python language of choice for Andriod?"
- Function Programming
    - "Why did you kill reduce()?"
    - "Please fix lambda."
    - "Please add more functional features."
- The Standard Library
    - "Why hasn't {my favorite package} been added to the standard library yet?"
- Garbage Collection
    - "Python doesn't have garbage collection."
    - "Reference counting is too slow."
- Language Evolution
    - "Stop changing the language already!"
    - "Please add {my favorite feature}!"

This is an old keynote. But if you didn't watch it and are interested with the trolls list above, go to watch it.
The video is on Youtube [1], But you can download it from my server[3], though I won't give my
guarantee on the link validity period.

And there is a recap for this keynote [4], I put it here:

--

Guido is wearing a "Python is for girls" T-shirt.

He showed a Python logo made out of foam on a latte. Yuko Honda really did it.

He had some comments about trolls.

Troll, n:
A leading question whose main purpose is to provoke an argument that cannot be won.
A person who asks such questions.
Guido said that Python, Ruby, and Perl are exactly the same language from 10,000 feet. They should be our friends. Lisp is not all that different from Python, although you might not notice it. Ruby is not kicking Python's butt in any particular case.

They added unicode literals back to Python 3.3 just to make compatibility with Python 2.7 easier.

"I should have used a real presentation tool instead of Google Docs." (Doh! He's a Googler!)

More and more projects are being ported to Python 3.

People are actually capable of using one code base for Python 2.7 and Python 3.3. There's a helpful library called "Six".

The Python 3 migration is painful now, but it's going to be worth it.

If PyPy is faster than cPython, why not abandon cPython? No one is using PyPy in production. PyPy is still hard for people writing C extensions. cPython is still a great glue system (for Fortran, C, and random binary code). "PyPy still has a long way to go. Speed is not everything." PyPy and cPython will live together in slightly different contexts for years. cPython will remain the reference implementation. 

People still criticize dynamic typing, saying it's not safe. "The type checking in compilers is actually really weak." For instance, most of the time, a type checker can't tell you if an int represents inches or centimeters. The only way to create good code is to test, audit, hire smart people, etc. Test! A type checking compiler can only find a narrow set of errors; no one has conquered the problem of writing perfect software.

A large program written in a statically typed language will often have a dynamically typed, interpreted subsystem, done via string manipulation, or something else.

Dynamic typing is not inherently inferior to static typing.

Guido hopes people are "doing interesting things with static analysis."

Guido pronounces GIL as "Jill".

"OS level threads are meant for parallel IO, not for parallel computation." Use separate processes for each core. One team was using Python on a machine with 64,000 cores. "You have to be David Beazley to come up with the counterexample."

Guido has complaints about each of the async libraries, but he doesn't have a solution that he recommends. It's not a problem he has to deal with. gevent is interesting. He can't add stackless to Python because it would make other implementations much more complicated or impossible. He doesn't want to put an event loop in the stdlib because not everyone needs it. Some things are better developed outside of Python. He's not a fan of callback-style approaches; he would prefer the gevent approach. He likes synchronous looking code that under the hood does async, without using threads. All these things deserve more attention.

We might want to make Python 4 the new language to solve the concurrent programming problem. He wants to see lots of alternatives.

Introducting a new language to replace JavaScript is such a hard, political problem.

He was told running Python on Android is "strategically not important." He was asked not to work on it anymore. Other people are going to have to do it.

"I don't think Python is a functional programming language. map, filter, lambda are not enough to make a functional programming language. Python is very pragmatic. It lets you mess around with state, fiddle with the OS, etc. Those things are really hard in a beautiful language like Haskell. When you have to do messy IO in Haskell, all the messiness becomes even messier.

Learn a functional language, get excited about the ideas, and let it impact your Python code. You don't have to do everything with a functional style.

"From data to data" really fits the functional paradigm. You can use that in Python.

He likes functional programming as a challenge and as an idea. However, 30 years from now, we won't all be writing functional programs all the time.

You're much better off not being in the stdlib. If you have a broken API, you can never fix it. Python has a very slow release schedule. It's much better to be third-party. Don't feel like you're not successful unless you're in the stdlib. It's better to own your own release cycle. Things in the stdlib should be things that enable everything else; like a context manager.

Python has reference counting and a garbage collector that resolves cycles, etc. PyPy is the place to play with better memory allocators. "I'm very happy with cPython's memory allocator."

Let's set our expectations low about adding new features to the language since we just finished Python 3. If you really have a desperate need for an extension to the language, think about using a preprocessor [my term] of some sort. Import hooks can let you do the transformation automatically.

[1] <https://www.youtube.com/watch?v=EBRMq2Ioxsc>  
[2] Guido is working at Dropbox now  
[3] http://kindle.io/media/videos/guido-python-2012.flv  
[4] [PyCon 2012 Keynote of Guido Van Rossum](http://jjinux.blogspot.jp/2012/03/pycon-keynote-guido-van-rossum.html)