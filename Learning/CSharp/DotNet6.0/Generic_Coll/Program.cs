string[] str = new string[] { "one", "five", "ten" };
Stack<string> stack = new Stack<string>(str);
foreach (string s in stack)
    Console.WriteLine(s);

SortedSet<int> sc = new SortedSet<int> { 1, 2, 3, 8, 8, 7, 5, 4, 2, 0 };
foreach (int s in sc)
    Console.Write(s);
Console.WriteLine();

Dictionary<int, string> dic = new Dictionary<int, string>()
{
    {1, "one" }, {2, "two"}, {3,"three"}
};
Dictionary<int, string>.KeyCollection number_keys = dic.Keys;
foreach (int n in number_keys)
    Console.WriteLine($"Key:{n}");

Dictionary<int, string> number = new Dictionary<int, string>();
number.Add(1, "one");
number.Add(2, "two");
number.Add(3, "three");
//number.Add(1,"four"); -> Error
Console.WriteLine(number[1]);