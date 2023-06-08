#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <io.h>

int main()
{
    char fn[] = "data.txt";
    int fd = open(fn, O_RDONLY);
    printf("File length : %d", filelength(fd));
    close(fd);
    system("pause");
    return 0;
}