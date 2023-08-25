int tmp;
int[] num = { 3, 6, 9, 5, 7 };
bool sorted;

for (int i = 1; i < num.Length; i++)
{
    sorted = true;
    for (int j = 0; j < (num.Length - 1); j++)
    {
        if (num[j] > num[j + 1])
        {
            tmp = num[j];
            num[j] = num[j + 1];
            num[j + 1] = tmp;
            sorted = false;
        }
    }
    if (sorted)
        break;
    Console.Write($"loop {i} ");
    foreach (int n in num)
        Console.Write($"{n,4}");
    Console.WriteLine("");
}