using System.Text.RegularExpressions;

string str = "0asd0235";
string pattern = "\\d{4}";
bool check = Regex.IsMatch(str, pattern);
if (check)
    Console.WriteLine($"{str} has a number(0~9)");
else
    Console.WriteLine("No number");