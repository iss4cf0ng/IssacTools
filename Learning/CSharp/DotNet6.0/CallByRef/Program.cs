void Swap(ref int x, ref int y)
{
    int tmp;
    tmp = x;
    x = y;
    y = tmp;
}

int x = 5;
int y = 1;
Console.WriteLine($"x={x} y={y}");
Swap(ref x, ref y);
Console.WriteLine($"x={x} y={y}");