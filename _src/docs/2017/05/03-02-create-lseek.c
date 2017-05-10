#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int
main() {
    char    buf1[] = "abcdefghij";
    char    buf2[] = "ABCDEFGHIJ";

    int fd = creat("file.hole", FILESEC_MODE);
    write(fd, buf1, 10);
    lseek(fd, 16384, SEEK_SET);
    write(fd, buf2, 10);
}
