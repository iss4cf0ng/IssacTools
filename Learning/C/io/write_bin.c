#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 5;
    float y = 10.5;
    int z[] = {8,10,12,14,16};
    FILE *stream;

    stream = fopen("output.bin", "wb");
    fwrite(&x, sizeof(int), 1, stream);
    fwrite(&y, sizeof(float), 1, stream);
    fwrite(z, sizeof(int), 5, stream);
    fclose(stream);
    system("pause");
    return 0;
}