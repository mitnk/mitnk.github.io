APUE Note - File I/O
====================

Notes of [APUE](https://www.amazon.com/Advanced-Programming-UNIX-Environment-3rd/dp/0321637739)

Most file I/O can be performed using only five functions: open, read, write,
lseek, and close. **Unbuffered** IO means that each read or write invokes a
system call in the kernel. These unbuffered I/O functions are not part of
ISO C, but are part of POSIX.1.

## File Descriptors

To the kernel, all open files are referred to by file
descriptors - non-negative integer. When we open an existing file or
create a new file, the kernel returns a file descriptor to the process.

## open/creat Functions

    :::c
    #include <fcntl.h>
    int open(const char *path, int oflag, ... /* mode_t mode */ );
    int creat(const char *path, mode_t mode);
    /* Both return: file descriptor if OK, −1 on error */

Note that `creat` is equivalent to

    :::c
    open(path, O_WRONLY | O_CREAT | O_TRUNC, mode);

## close function

When a process terminates, all of its open files are closed automatically
by the kernel.

## lseek Function

Because a successful call to lseek returns the new file offset, we can
seek zero bytes from the current position to determine the current offset:

    :::c
    off_t    currpos;
    currpos = lseek(fd, 0, SEEK_CUR);

This technique can also be used to determine if a file is capable of seeking.
If the file descriptor refers to a pipe, FIFO, or socket, lseek sets errno
to ESPIPE and returns −1.

    :::c
    #include <stdio.h>
    #include <unistd.h>

    int
    main(void) {
        if (lseek(STDIN_FILENO, 0, SEEK_CUR) == -1) {
            printf("cannot seek\n");
        } else {
            printf("seek ok\n");
        }
    }

Test:

    $ ./a.out < /etc/passwd
    seek OK
    $ cat < /etc/passwd | ./a.out
    cannot seek

### Copy a file - using only read and write

    :::c
    #include <stdio.h>
    #include <unistd.h>

    #define BUFFSIZE 4096

    int
    main(void) {
        int n;
        char buf[BUFFSIZE];
        while ((n = read(0, buf, BUFFSIZE)) > 0) {
            write(1, buf, n);
        }
    }

Test:

    $ cc 03-03-copy.c
    $ ./a.out < foo.txt > bar.txt

Changing `BUFFSIZE` in it can test IO efficiency. From 1 byte to 512k bytes.
We found from 1024, the timing are quite the same.


## Atomic Operations

The UNIX System provides an atomic way to do this operation if we set
the `O_APPEND` flag when a file is opened. As we described in the previous
section, this causes the kernel to position the file to its current end of
file before each write. We no longer have to call lseek before each write.

See `pread` and `pwrite` Functions.


## dup and dup2 Functions

The call `dup(fd);` is equivalent to `fcntl(fd, F_DUPFD, 0);`. Similarly,
the call `dup2(fd, fd2);` is equivalent to
`close(fd2); fcntl(fd, F_DUPFD, fd2);`.

`dup2` is an atomic operation, whereas the alternate form involves two
function calls.

## sync, fsync, and fdatasync Functions

Traditional implementations of the UNIX System have a buffer cache or
page cache in the kernel through which most disk I/O passes. When we write
data to a file, the data is normally copied by the kernel into one of its
buffers and queued for writing to disk at some later time. This is called
delayed write.

## fcntl Function

The fcntl function can change the properties of a file that is already open.

    :::c
    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <fcntl.h>

    int
    main(int argc, char *argv[])
    {
        int val;
        if (argc != 2)
            printf("usage: a.out <descriptor#>\n");
        val = fcntl(atoi(argv[1]), F_GETFL, 0);
        switch (val & O_ACCMODE) {
            case O_RDONLY:
                printf("read only");
                break;
            case O_WRONLY:
                printf("write only");
                break;
            case O_RDWR:
                printf("read write");
                break;
            default:
                printf("unknown access mode\n");
        }
        if (val & O_APPEND)
            printf(", append");
        if (val & O_NONBLOCK)
            printf(", nonblocking");
        if (val & O_SYNC)
            printf(", synchronous writes");
    #if !defined(_POSIX_C_SOURCE) && defined(O_FSYNC) && (O_FSYNC != O_SYNC)
        if (val & O_FSYNC)
            printf(", synchronous writes");
    #endif
        putchar('\n');
        exit(0);
    }

Test:

    $ cc 03-04-fcntl.c
    $ ./a.out 0 < /dev/tty
    read only
    $ ./a.out 1 > temp.foo
    $ cat temp.foo
    write only


## ioctl Function

The `ioctl` function has always been the catchall for I/O operations. Anything
that couldn’t be expressed using one of the other functions in this chapter
usually ended up being specified with an ioctl. Terminal I/O was the biggest
user of this function.

## /dev/fd

Newer systems provide a directory named `/dev/fd` whose entries are files
named 0, 1, 2, and so on. Opening the file `/dev/fd/n` is equivalent to
duplicating descriptor `n`, assuming that descriptor n is open.
