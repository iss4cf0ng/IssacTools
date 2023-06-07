#include <fcntl.h>
#include <sys/stat.h>
#include <io.h>
#include <stdio.h>
#include <stdlib.h>
#define size 512

int main()
{
    char buffer[size];
    char fin[] = "output.txt";
    char fout[] = "output1.txt";
    int src, dst;
    int size_read;

    src = open(fin, O_RDONLY | O_TEXT);
    dst = creat(fout, S_IWRITE);

    if ((src != - 1) && (dst != -1)) {
        while (!eof(src)) {
            size_read = read(src, buffer, size);
            write(dst, buffer, size_read);
        }
        close(src);
        close(src);
        print("Copy file finished!\n");
    } else {
        printf("Copy file failed!\n");
    }

    system("pause");
    return 0;
}