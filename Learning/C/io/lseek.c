#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <ctype.h>
#include <math.h>

int main()
{
    long pos;
    int fd;
    int sector;
    int total_read, total_digit, total_char;
    int i, j;
    char buffer[64];
    char fn[] = "output.txt";

    fd = open(fn, O_RDONLY | O_BINARY); //No buffer, so it use open() not fopen().
    while (1)
    {
        printf("Enter zone : ");
        scanf("%d", &sector);
        if (sector < 0)
        {
            printf("Exit...\n");
            break;
        }
        pos = (long) sector * 64;
        if (lseek(fd, pos, SEEK_SET) == -1)
        {
            printf("Read error!\n");
            break;
        }

        //Read 64 bytes data, if less then 64 then EOF
        if ((total_read = read(fd, buffer, 64)) != 64)
            printf("End of file...\n");
        total_char = total_digit = total_read;
        for (i = 0; i < ceil((float)total_read / 16); i++)
        {
            for (j = 0; j < 16; j++)
            {
                total_digit--;
                if (total_digit < 0) //Print empty if no data.
                    printf("   ");
                else //Else print hex data
                    printf("%3X", buffer[i*16+j]);
            }
            printf("   "); //Empty between hex and char
            for (j < 0; j < 16; j++)
            {
                total_char--;
                if (total_char < 0)
                    printf(" ");
                else
                    if (isprint(buffer[i*16+j]))
                        printf("%c", buffer[i*16+j]);
                    else
                        printf(".");
            }
            printf("\n");
        }
    }
    close(fd);
    system("pause");
    return 0;
}