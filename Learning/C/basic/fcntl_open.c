#include <fcntl.h>
#include <sys/stat.h>
#include <io.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int fd;
    if ((fd == open("output.txt", O_RDONLY)) != -1) {
        printf("Open file OK!\n");
    } else {
        printf("Open file failed!\n");
        exit(1);
    }

    if (close(fd) != -1) {
        printf("Close file OK\n");
    } else {
        printf("Close file failed\n");
    }
    system("pause");
    return 0;
}