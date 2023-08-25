void CountA(string str, out int counter)
{
    counter = 0;
    for (int i = 0; i < str.Length; i++)
        if (str[i] == 'A')
            counter++;
}

int num;
Console.Write("Enter a string: ");
string str = Console.ReadLine();
CountA(str, out num);
Console.WriteLine(num);