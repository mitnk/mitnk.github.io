APUE Note - Standard I/O Library
================================

Notes of [APUE](https://www.amazon.com/Advanced-Programming-UNIX-Environment-3rd/dp/0321637739)

With the standard I/O library, the discussion centers on streams. When we
open or create a file with the standard I/O library, we say that we have
associated a stream with the file.

## Buffering

The goal of the buffering provided by the standard I/O library is to use
the minimum number of `read` and `write` calls.

With setbuf, we can turn buffering on or off.

    :::c
    #include <stdio.h>
    void setbuf(FILE *restrict fp, char *restrict buf);

## Opening a Stream

    :::c
    #include <stdio.h>
    FILE *fopen(const char *restrict pathname, const char *restrict type);
    FILE *freopen(const char *restrict pathname, const char *restrict type,
                  FILE *restrict fp);
    FILE *fdopen(int fd, const char *type);

## Reading and Writing a Stream

Three functions allow us to read one character at a time.

    :::c
    #include <stdio.h>
    int getc(FILE *fp);
    int fgetc(FILE *fp);
    int getchar(void);

The difference between `getc` and `fgetc` is that getc can be implemented as
a macro, whereas fgetc cannot be implemented as a macro. This means
three things.

- The argument to getc should not be an expression with side effects,
  because it could be evaluated more than once.
- Since fgetc is guaranteed to be a function, we can take its address.
  This allows us to pass the address of fgetc as an argument to another function.
- Calls to fgetc probably take longer than calls to getc,
  as it usually takes more time to call a function.

### Output Functions

    :::c
    #include <stdio.h>
    int putc(int c, FILE *fp);
    int fputc(int c, FILE *fp);
    int putchar(int c);

## Line-at-a-Time I/O

Line-at-a-time input is provided by the two functions, `fgets` and `gets`.
Line-at-a-time output is provided by `fputs` and `puts`.

## Standard I/O Efficiency

    :::c
    #include <stdio.h>
    int main()
    {
        int c;
        while ((c = getc(stdin)) != EOF)
            putc(c, stdout);
    }

with reads/writes lines

    :::c
    #include <stdio.h>
    #define MAXLINE 4096

    int main()
    {
        char buf[MAXLINE];
        while (fgets(buf, MAXLINE, stdin) != NULL)
            fputs(buf, stdout);
    }

After testing, we’ve learned that the standard I/O library is not much slower
than calling the read and write functions directly.

## Binary I/O

The following two functions are provided for binary I/O.

    :::c
    #include <stdio.h>
    size_t fread(void *restrict ptr, size_t size, size_t nobj,
                 FILE *restrict fp);
    size_t fwrite(const void *restrict ptr, size_t size, size_t nobj,
                  FILE *restrict fp);

These functions have two common uses:

    :::c
    /* to write elements 2 through 5 of a floating-point array */
    float data[10];
    fwrite(&data[2], sizeof(float), 4, fp);

    /* Read or write a structure */
    struct {
        short  count;
        long   total;
        char   name[NAMESIZE];
    } item;
    fwrite(&item, sizeof(item), 1, fp);

A fundamental problem with binary I/O is that it can be used to read only
data that has been written on the same system.

## Positioning a Stream

TBC.
