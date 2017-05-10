APUE Note - Files and Directories
=================================

Notes of [APUE](https://www.amazon.com/Advanced-Programming-UNIX-Environment-3rd/dp/0321637739)

## stat, fstat, fstatat, and lstat Functions

The biggest user of the stat functions is probably the `ls -l` command, to
learn all the information about a file.

## File Types

- Regular file
    * The most common type of file, which contains data of some form. There is
      no distinction to the UNIX kernel whether this data is text or binary.
- Directory file
    * A file that contains the names of other files and pointers to
      information on these files. Any process that has read permission
      for a directory file can read the contents of the directory,
      but only the kernel can write directly to a directory file. Processes
      must use the functions to make changes to a directory.
- Block special file
    * A type of file providing buffered I/O access in fixed-size units to
      devices such as disk drives.
- Character special file
    * A type of file providing unbuffered I/O access in variable-sized
      units to devices.
- FIFO
    * A type of file used for communication between processes. It’s
      sometimes called a named pipe.
- Socket
    * A type of file used for network communication between processes.
- Symbolic link
    * A type of file that points to another file.

Prints the type of file for each command-line argument:

    :::c
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/stat.h>

    int main(int argc, char *argv[])
    {
        int i;
        struct stat buf;
        char *ptr;
        for (i = 1; i < argc; ++i) {
            printf("%s: ", argv[i]);
            if (lstat(argv[i], &buf) < 0) {
                printf("lstat error\n");
                continue;
            }

            if (S_ISREG(buf.st_mode))
                ptr = "regular";
            else if (S_ISDIR(buf.st_mode))
                ptr = "directory";
            else if (S_ISCHR(buf.st_mode))
                ptr = "character special";
            else if (S_ISBLK(buf.st_mode))
                ptr = "block special";
            else if (S_ISFIFO(buf.st_mode))
                ptr = "fifo";
            else if (S_ISLNK(buf.st_mode))
                ptr = "symbolic link";
            else if (S_ISSOCK(buf.st_mode))
                ptr = "socket";
            else
                ptr = "** unknown mode **";
            printf("%s\n", ptr);
        }
    }

Test:

    $ ./a.out /etc/passwd /etc /dev/log /dev/tty
    /etc/passwd: regular
    /etc: symbolic link
    /dev/log: lstat error
    /dev/tty: character special

## access and faccessat Functions

The use of the access function

    :::c
    #include <stdio.h>
    #include <unistd.h>
    #include <fcntl.h>
    #include <sys/stat.h>

    int main(int argc, char *argv[])
    {
        if (argc != 2)
            printf("usage: a.out <pathname>\n");
        if (access(argv[1], R_OK) < 0)
            printf("access error for %s\n", argv[1]);
        else
            printf("read access OK\n");
        if (open(argv[1], O_RDONLY) < 0)
            printf("open error for %s\n", argv[1]);
        else
            printf("open for reading OK\n");
    }


Test

    $ ./a.out a.out
    read access OK
    open for reading OK
    $ ./a.out /etc/shadow
    access error for /etc/shadow
    open error for /etc/shadow

## umask Function

The umask function sets the file mode creation mask for the process and
returns the previous value. Any bits that are on in the file mode creation
mask are turned off in the file’s mode. The umask() function is always
successful.

    :::c
    #include <stdio.h>
    #include <sys/stat.h>
    #include <fcntl.h>

    #define RWRWRW (S_IRUSR|S_IWUSR|S_IRGRP|S_IWGRP|S_IROTH|S_IWOTH)

    int main()
    {
        umask(0);
        if (creat("foo", RWRWRW) < 0)
            printf("creat error for foo\n");
        umask(S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH);
        if (creat("bar", RWRWRW) < 0)
            printf("creat error for bar\n");
    }

Test

    $ ls -l foo bar
    -rw-------  1 mitnk  staff  0 May 10 19:41 bar
    -rw-rw-rw-  1 mitnk  staff  0 May 10 19:41 foo

## chmod, fchmod, and fchmodat Functions

    :::c
    #include <stdio.h>
    #include <sys/types.h>
    #include <sys/stat.h>

    int main()
    {
        struct stat statbuf;

        /* turn on set-group-ID and turn off group-execute */
        if (stat("foo", &statbuf) < 0)
            printf("stat error for foo\n");
        if (chmod("foo", (statbuf.st_mode & ~S_IXGRP) | S_ISGID) < 0)
            printf("chmod error for foo\n");

        /* set absolute mode to "rw-r--r--" */
        if (chmod("bar", S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH) < 0)
            printf("chmod error for bar\n");
    }

Test

    $ ./a.out
    $ ls -l foo bar
    -rw-r--r--  1 mitnk  staff  0 May 10 19:41 bar
    -rw-rwSrw-  1 mitnk  staff  0 May 10 19:41 foo

## chown, fchown, fchownat, and lchown Functions

The chown functions allow us to change a file’s user ID and group ID.

## File Size

The `st_size` member of the stat structure contains the size of the file in
bytes. This field is meaningful only for regular files, directories, and
symbolic links.

For a symbolic link, the file size is the number of bytes in the filename.

## Holes in a File

    $ ls -l core
    -rw-r--r-- 1 sar 8483248 Nov 18 12:18 core
    $ du -s core
    272 core
    $ wc -c core
    8483248 core

## File Truncation

Sometimes we would like to truncate a file by chopping off data at the end
of the file. `truncate` and `ftruncate` are for this.

## link, linkat, unlink, unlinkat, and remove Functions

Opens a file and then unlinks it.


    :::c
    #include <stdio.h>
    #include <sys/stat.h>
    #include <unistd.h>
    #include <fcntl.h>

    int main() {
        if (open("tempfile", O_RDWR) < 0)
            printf("open error\n");
        if (unlink("tempfile") < 0)
            printf("unlink error\n");
        printf("file unlinked\n");
        sleep(15);
        printf("done\n");
    }

The process creates a file using either `open` or `creat` and then
immediately calls `unlink`. The file is not deleted, however, because it is
still open. Only when the process either closes the file or terminates,
which causes the kernel to close all its open files, is the file deleted.

## futimens, utimensat, and utimes Functions

truncates files to zero length using the `O_TRUNC` option of the open
function, but does not change their access time or modification time.
To do this, the program first obtains the times with the stat function,
truncates the file, and then resets the times with the futimens function.

    
