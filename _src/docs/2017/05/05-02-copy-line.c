#include <stdio.h>
#define MAXLINE 4096

int main()
{
    char buf[MAXLINE];
    while (fgets(buf, MAXLINE, stdin) != NULL)
        fputs(buf, stdout);
}
