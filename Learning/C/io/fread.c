#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *stream;
    char var;

    stream = fopen("output.txt", "rb");
    while (fread(&var, sizeof(var), 1, stream) != 0)
    {
        printf("%c", var);
    }
    fclose(stream);
    system("pause");
    return 0;
}