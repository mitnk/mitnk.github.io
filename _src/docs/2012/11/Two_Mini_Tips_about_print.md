With the following code, we accomplished two stuff:

1. print multiple part of content in one single line in Python3
2. print a char per time without blocking in one single line

--

    :::python
    import time
    import sys

    def delay_print(s):
        for c in s:
            print(c, end='')
            sys.stdout.flush()
            time.sleep(0.25)
        print()

    delay_print("hello world")

This code is written for **Python3**, NOT for Python2.X.