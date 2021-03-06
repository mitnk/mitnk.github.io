Notes on C Language
===================

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


## Three types of memory; three bundles of features

    :::
    +------------------------------------+--------+------+--------+
    |                                    | Static | Auto | Manual |
    +------------------------------------+--------+------+--------+
    | Set to zero on startup             | Y      |      |        |
    |                                    |        |      |        |
    | Scope-limited                      | Y      | Y    |        |
    |                                    |        |      |        |
    | Can set value on init              | Y      | Y    |        |
    |                                    |        |      |        |
    | Can set nonconstant values on init |        | Y    |        |
    |                                    |        |      |        |
    | sizeof measures array size         | Y      | Y    |        |
    |                                    |        |      |        |
    | Persists across function calls     | Y      |      | Y      |
    |                                    |        |      |        |
    | Can be global                      | Y      |      | Y      |
    |                                    |        |      |        |
    | Array size can be set at runtime   |        | Y    | Y      |
    |                                    |        |      |        |
    | Can be resized                     |        |      | Y      |
    |                                    |        |      |        |
    | Jesus weeps                        |        |      | Y      |
    +------------------------------------+--------+------+--------+

## C Pointers

When a program runs across this declaration in your code:

    :::c
    int an_array[32];

the program will:

- set aside a space on the stack big enough for 32 integers,
- declare that an_array is a pointer, and
- bind that pointer to point to the newly allocated space.

When a program runs across this declaration in your code:

    :::c
    int *a_pointer;

the program will only do one of the above steps:

- declare that an_array is a pointer

This pointer is not bound to any specific location in memory, and so is free to be
assigned to point to anywhere. Valid uses include:

    :::c
    //manually allocating a new block; pointing a_pointer to it:
    a_pointer = malloc(32*sizeof(int));

    //pointing the pointer to an_array, as declared above.
    a_pointer = an_array;

In other cases, such as in a typedef declaration (such as for a new struct)
or a function call, there is less distinction to be made:

    :::c
    int f(int *a_pointer, int an_array[]);

a_pointer and an_array behave identically.

The Fibonacci sequence generated by a state machine (fibo.c)

    :::c
    #include <stdio.h>

    long long int fibonacci() {
        static long long int first = 0;
        static long long int second = 1;
        long long int out = first+second;
        first=second;
        second=out;
        return out;
    }

    int main() {
        for (int i = 0; i < 50; i++)
            printf("%lli\n", fibonacci());
    }

Static variables, even those inside of a function, are initialized when
the program starts, before main, so you can’t initialize them with
a nonconstant value.

    :::c
    //this fails: can't call gsl_vector_alloc() before main() starts
    static gsl_vector *scratch = gsl_vector_alloc(20);

This is an annoyance, but easily solved with a macro to start at zero
and allocate on first use:

    :::c
    #define Staticdef(type, var, initialization) \
        static type var = 0; \
        if (!(var)) var = (initialization);

    //usage:
    Staticdef(gsl_vector*, scratch, gsl_vector_alloc(20));

This works as long as we don’t ever expect initialization to be zero
(or in pointer- speak, NULL). If it is, it’ll get reinitialized on the
next go-round. Maybe that’s OK any‐ way.

To give another example where malloc sometimes needlessly turns up,
you may have a function that takes in a pointer as input:

    :::c
    void increment(int *i) {
        (*i)++;
    }

Users of the function who too closely associate pointers with malloc
might think that this means that they have to allocate memory to
pass in to the function:

    :::c
    int *i = malloc(sizeof(int)); // so much effort, wasted
    *i = 12;
    increment(i);
    ...
    free(i);

Rather, the easiest use is to let automatic memory allocation do the work:

    :::c
    int i=12; increment(&i);

### Structures Get Copied, Arrays Get Aliased

Copying the contents of a structure is a one-line operation

    :::c
    #include <stdio.h>
    #include <assert.h>

    typedef struct {
        int a, b;
        double c, d;
        int *efg;
    } demo_s;

    int main() {
        demo_s d1 = {.b=1, .c=2, .d=3, .efg=(int[]){4,5,6}};
        demo_s d2 = d1;
        d1.b = 14;
        d1.c = 41;
        d1.efg[0] = 7;

        // all these asserts will pass
        assert(d2.a == 0);
        assert(d2.b == 1);
        assert(d2.c == 2);
        assert(d2.d == 3);
        assert(d2.efg[0] == 7);

        // For arrays, the equals sign will copy an alias
        int abc[] = {0, 1, 2};
        int *copy = abc;

        copy[0] = 3;
        assert(abc[0]==3);  // passes

        printf("OK.\n");
    }

when we change d1.efg[0], the change also affects the copy of a pointer
d2.efg. This advises that if you need a deep copy where pointer
contents are copied, you will need a struct copying function, and if
you don’t have any pointers to trace through, then a copy function is
overkill and an equals sign will do.

A function that ends in return x will return the value of x to the
calling function [C99 and C11 §6.8.6.4(3)]. Seems simple enough,
but that value has to be copied out to the calling function, whose frame
is about to be destroyed. As previously, for a struct, a number,
or even a pointer, the calling function will get a copy of the
returned value; for an array, the calling function will get a pointer
to the array, not a copy of the data in the array.

    :::c
    #include <stdio.h>
    typedef struct powers {
        double base, square, cube;
    } powers;

    powers get_power(double in) {
        // The initialization is via designated initializers
        powers out = {
            .base   = in,
            .square = in*in,
            .cube   = in*in*in
        };
        // This is valid. On exit, a copy of the local, automatically
        // allocated out is made, then the local copy is destroyed.
        return out;
    }


    int *get_even(int count) {
        int out[count];
        for (int i=0; i< count; i++)
            out[i] = 2*i;
        // This is invalid. Here, arrays really are treated like pointers,
        // so on exit, a copy of the pointer to out gets made.
        // But once the autoallocated memory is destroyed, the pointer is
        // now pointing to bad data.
        return out;
    }

    int main(){
        powers threes = get_power(3);
        printf("threes: %g\t%g\t%g\n", threes.base, threes.square, threes.cube);

        // evens is a valid pointer-to-int, but it is pointing to
        // already freed data. This may segfault, print garbage,
        // or get lucky and print the correct values (this time).

        // int *evens = get_even(3);
        // printf("evens: %i\t%i\t%i\n", evens[0], evens[1], evens[2]);
    }


If you need a copy of an array, you can still do it on one line:

    :::c
    #include <assert.h>
    #include <stdio.h>
    #include <string.h> // memmove

    int main(){
        int A[] = {0, 1, 2};
        int *copy1, copy2[3];

        copy1 = A;
        memmove(copy2, A, sizeof(int) * 3);

        A[0] = 3;
        assert(copy1[0] == 3);
        assert(copy2[0] == 0);

        printf("OK.\n");
    }

### malloc and Memory-Twiddling

The easiest way to avoid bugs related to malloc is not to use malloc.
Historically, we needed malloc for all sorts of string manipulations;
we needed malloc to deal with arrays for which length had to be set
at runtime, which is pretty common; is also largely obsolete.


    :::c
    int *i = malloc(sizeof(int)); // right
    *i = 23; // right
    int *i = 23; // wrong

    // valid snippet
    inti = 13;
    int*j = &i;
    int*k = j;
    *j = 12;


### All the Pointer Arithmetic You Need to Know


Declare a pointer `double *p`, `p[1]` is exactly equivalent to `*(p+1)`.

- Declare arrays either via the explicit pointer form,
    `double *p` or the static/automatic form, `double p[100]`
- In either case, the nth array item is `p[n]`. Don’t forget that
    the first item is zero, not one; it can be referred to
    with the special form `p[0] == *p`
- If you need the address of the nth element (not its actual value),
    use the ampersand: `&p[n]`. Of course, the zeroth pointer is
    just `&p[0] == p`

The fact that p++ means “step to the next pointer”

    :::c
    #include <stdio.h>

    int main(){
        char *A[] = {"one", "two", "three", NULL};
        for (char **s = A; *s != NULL; ++s) {
            printf("elmt: %s\n", *s);
        }
    }

Base-plus-offset thinking doesn’t give us much payoff in terms of cute
syntactic tricks, but it does explain a lot about how C works.
In fact, consider the struct. Given:

    :::c
    typedef struct {
        int a, b;
        double c, d;
    } abcd_s;
    abcd_s list[3];

As a mental model, you can think of list as our base, and `list[0].b`
is just far enough past that to refer to `b`. That is, given that the
location of list is the integer `(size_t)&list`, `b` might be located at
`(size_t)&list + sizeof(int)`; and so `list[2].d` would be at the position
`(size_t)&list + 6*sizeof(int) + 5*sizeof(double)`. Under this thinking,
a struct is much like an array, except the elements have names instead of
numbers and are of different types and sizes.

It’s not quite correct, because of alignment: the system may decide that
the data needs to be in chunks of a certain size, so fields may have extra
space at the end so that the next field begins at the right point, and the
struct may have padding at its end so that a list of structs is
appropriately aligned [C99 and C11 §6.7.2.1(15) and (17)]. The header
`stddef.h` defines the `offsetof` macro, which makes the base-plus-offset
thinking accurate again: `list[2].d` really is at
`(size_t)&list + 2*sizeof(abcd_s) + offsetof(abcd_s, d)`.

By the way, there can’t be padding at the beginning of a struct,
so `list[2].a` is at `(size_t)&list+ 2*sizeof(abcd_s)`.


### Typedef as a teaching tool

    :::c
    #include <stdio.h>
    typedef char* string;

    int main(){
        string A[] = {"one", "two", "three", NULL};
        for (string *s = A; *s != NULL; ++s) {
            printf("elmt: %s\n", *s);
        }
    }

Typedefs save the day when dealing with pointers to functions. If you have
a function with a header like:

    :::c
    double a_fn(int, int); // a declaration

then just add a star (and parens to resolve precedence) to describe a
pointer to this type of function:

    :::c
    double (*a_fn_type)(int, int); // a type: pointer-to-function

Then put typedef in front of that to define a type:

    :::c
    typedef double (*a_fn_type)(int, int); // a typedef for a pointer to function

Now you can use it as a type like any other, such as to declare a
function that takes another function as input:

    :::c
    double apply_a_fn(a_fn_type f, int first_in, int second_in) {
        return f(first_in, second_in);
    }

## Inessential C Syntax

**Don’t Bother Explicitly Returning from `main`**

### Set Array Size at Runtime

Old way:

    :::c
    pthread_t *threads;
    int thread_count;
    thread_count = atoi(argv[1]);
    threads = malloc(thread_count * sizeof(pthread_t));
    ...
    free(threads);

Can be replaced with:

    :::c
    int thread_count = atoi(argv[1]);
    pthread_t threads[thread_count];

In the 1970s and 1980s, malloc returned a char* pointer and had to
be cast (unless you were allocating a string), with a form like:

    :::c
    //don't bother with this sort of redundancy:
    double* list = (double*) malloc(list_length * sizeof(double));

You don’t have to do this anymore, because malloc now gives you a void
pointer, which the compiler will comfortably autocast to any pointer type.

    :::c
    int use_parameters(void *params_in){
        // Effectively casting pointer-to-NULL
        // to a pointer-to-param_struct.
        param_struct *params = params_in;
        ...
    }

### Enums and Strings

Enums are a good idea that went bad.

There are reasons for using enums: sometimes you have an array that
makes no sense as a struct but that nonetheless requires named elements,
and when doing kernel- level work, giving names to bit patterns is essential.
But in cases where enums are used to indicate a short list of options or
a short list of error codes, a single character or a short string can
serve the purpose without cluttering up the namespace or users’ memory.

So, to revise the common wisdom on goto, it is generally harmful but
is a common present-day idiom for cleaning up in case of different kinds
of errors, and it is often cleaner than the alternatives.

### Deprecate Float

use double instead of float, and for intermediate values in calculations,
it doesn’t hurt to use long double.

There are several functions available to parse the numeric value of
a string of text. The most popular are atoi and atof
(ASCII-to-int and ASCII-to-float). The safer alternative is using
`strtol` and `strtod`.


## Important C Syntax that Textbooks Often Do Not Cover




--------------

Note from: [21st Century C: C Tips from the New School](http://www.amazon.com/gp/product/1491903899/)
