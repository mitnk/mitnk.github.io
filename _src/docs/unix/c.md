C - Compile Make Debug and Document
===================================

## Link libraries when compiling

To use a library, you have to tell the compiler that you will be
importing functions from the library twice: once for the compilation and
once for the linker. For a library in a standard location,
the two declarations happen via an `#include` in the text of the program and
a `-l` flag on the compiler line.

    :::bash
    $ gcc erf.c -o erf -lm -g -Wall -O3 -std=gnu11
    $ gcc -I/usr/local/include use_useful.c -o use_useful -L/usr/local/lib -luseful

`-lm` tells the linker to link in the math library (math.h). `gcc` will
implicitly add a `-lc` at the end of command to link standard
`libc` library. `-g` adds symbols for debugging.
`-Wall` means "set Warnings to ALL". The functions in `stdlib.h`
and `stdio.h` have implementations in `libc.so`
(or `libc.a` for static linking), which is linked into your executable
by default (as if `-lc` were specified). `GCC` can be instructed to avoid
this automatic link with the `-nostdlib` or `-nodefaultlibs` options.
`-I` adds the given path to the include search path. -L adds to
the library search path.

Order matters. If you have a file named specific.o that depends on the
Libbroad library, and Libbroad depends on Libgeneral, then you will need:

    :::bash
    $ gcc specific.o -lbroad -lgeneral

### pkg-config

Can be installed by `brew`.

    :::bash
    $ pkg-config --libs openssl
    -lssl -lcrypto -lz

    $ pkg-config --libs libcurl openssl
    -L/usr/local/lib -lcurl -lssl -lcrypto -lz

    $ pkg-config --cflags libcurl
    -I/usr/local/include

Environment Variables in C

    :::c
    #include <stdlib.h> //getenv, atoi
    #include <stdio.h> //printf

    int main() {
        char *repstext = getenv("reps");
        int reps = repstext ? atoi(repstext) : 10;
        char *msg = getenv("msg");
        if (!msg)
            msg = "Hello.";
        for (int i=0; i< reps; i++)
            printf("%s\n", msg);
    }

### Makefile

(Use **Tabs** install spaces in the file)

    P=helloworld
    OBJECTS=
    CFLAGS = -g -O3 -Wall -Wextra -std=gnu11 -nostdlib -lc
    LDLIBS=
    CC=gcc

    $(P): $(OBJECTS)

    clean:
        @rm -f *.{o,out}
        @rm -rf *.dSYM/
        @rm -f $(P)

### What Are the Linker Flags for Building a Shared Library?

To tell you the truth, I have no idea. It’s different across operating
systems, both by type and by year, and even on one system the rules are
often hairy. Instead, Libtool, one of the tools introduced in Chapter 3,
knows every detail of every shared library generation procedure on every
operating system. I recommend invest‐ ing your time getting to know
Autotools and thus solve the shared object compilation problem once
and for all, rather than investing that time in learning the right
compiler flags and linking procedure for every target system.

### man

use man strtok to read about the strtok function, typically including what header to include, the input arguments, and basic notes about its usage. every manual page has a one-line summary, and man -k searchterm will search those summaries. Many systems also have the apropos command, which is similar to man -k. The manual is divided into sections. Section 1 is command-line commands, and section 3 is library functions. If your system has a command-line program named printf, then man printf will show its documentation, and man 3 printf will show the documentation for the C library’s printf command.

### Using Libraries from Source

    :::bash
    $ mkdir ~/root
    ./configure --prefix=$HOME/root && make && make install

to use:

    :::bash
    LDLIBS=-L$(HOME)/root/lib (plus the other flags, like -lgsl -lm ...)
    CFLAGS=-I$(HOME)/root/include (plus -g -Wall -O3 ...)

## Debug

Logic check with GDB, memory leaks check with Valgrind. Linus Torvalds explains: “I use gdb all the time ... as a disassembler on steroids that you can program.” Use the -g flag in the compiler switches, turning off optimization via the -O0 (oh zero) compiler flag, because the optimizer may eliminate variables useful for debugging and shuffle the code in surprising ways. I’ve always found debugging C++ code from the gdb prompt to be painful. Because C code compiles without mangling. On a Mac, you may need to run debug sessions via sudo.

    :::bash
    $ sudo pdb a.out

in your makefile, add:

    CFLAGS=-DTest_operations

The -D flag is the POSIX-standard compiler flag that is equivalent to putting #define Test_operations at the top of every .c file.

### The Stack of Frames

If your question is just “Where am I?” the easy answer is the line number in the code, and sometimes this is all you need. But more often, your question is “How did I get here?” and the answer, the backtrace or call stack, is a listing of the stack of frames. Here’s a sample backtrace:

    #0  0x00413bbe in agent_address (agent_number=312) at addresses.c:100
    #1  0x004148b6 in get_agents () at addresses.c:163
    #2  0x00404f9b in main (argc=1, argv=0x7fffffffe278) at addresses.c:227

### Valgrind

    $ valgrind your_program

You can also start the debugger at the first error, by running:

    $ valgrind --db-attach=yes your_program

Valgrind also does memory leaks:

    $ valgrind --leak-check=full your_program

This is typically slower, so you might not want to run it every time.

## Unit Testing

Use [GLib](https://developer.gnome.org/glib/)''s Test framework to do unit testing.

## Documentation

- Doxygen
- Graphviz
- CWEB

Note from: [21st Century C: C Tips from the New School](http://www.amazon.com/gp/product/1491903899/)
