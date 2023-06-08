#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int main()
{
    FILE *fp;
    int sector;
    int total_read, total_digit, total_char;
    int i, j;
    char buffer[64];
    char fn[] = "output.txt";

    fp = fopen(fn, "rb");
    while (1)
    {
        printf("Enter drive : ");
        scanf("%d", &sector);
        if (sector < 0)
        {
            printf("Exit...\n");
            break;
        }
        if (fseek(fp, sector * 64, 0) != 0)
        {
            printf("Read data failed!\n");
            break;
        }
        printf("\n");

        //Read 64 bytes everytime, if less then 64 then EOF.
        if ((total_read = fread(buffer, 1, 64, fp)) != 64)
            printf("End of file...\n");

        total_char = total_digit = total_read;
        for (i = 0; i < ceil((float)total_read / 16); i++)
        {
            for (j = 0; j < 16; j++)
            {
                total_digit--;
                if (total_digit < 0) //No data then print \r
                    printf("   ");
                else //Else print hex
                    printf("%3X", buffer[i*16 + j]);
            }
            printf("   "); //Empty between hex and char
            for (j = 0; j < 16; j++)
            {
                total_char--;
                if (total_char < 0)
                    printf(" "); //After print replaced by empty
                else //use dot replace non-char
                    if (isprint(buffer[i*16+j]))
                        printf("%c", buffer[i*16+j]);
                    else
                        printf(".");
            }
            printf("\n");
        }
    }
    fclose(fp);
    system("pause");
    return 0;
}