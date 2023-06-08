#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    float y;
    int z[5];
    FILE *stream;
    int i;

    stream = fopen("output.bin", "rb");
    fread(&x, sizeof(int), 1, stream);
    fread(&y, sizeof(float), 1, stream);
    fread(z, sizeof(int), 5, stream);
    fclose(stream);

    system("pause");
    return 0;
}