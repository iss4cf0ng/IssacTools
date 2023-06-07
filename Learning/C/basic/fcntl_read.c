#include <fcntl.h>
#include <sys/stat.h>
#include <io.h>
#include <stdlib.h>
#include <stdio.h>
#define SIZE 512

int main()
{
    int fd;
    char buf[SIZE];
    int count = 0;
    int i;
    char fn[] = "output.txt";

    fd = open(fn, O_RDONLY);
    while ((i = read(fd, buf, SIZE)) > 0)
        count += i;
    printf("%s char number is : %d\n", fn, count);
    close(fd);
    system("pause");
    return 0;
}