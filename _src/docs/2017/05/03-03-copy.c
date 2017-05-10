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
