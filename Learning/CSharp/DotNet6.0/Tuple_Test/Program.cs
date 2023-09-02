Tuple<string, char, int> person1 = new Tuple<string, char, int>("Petter", 'M', 15);
Console.WriteLine(person1);
Console.WriteLine(person1.Item1);

var number = ("one", "two", "three", 4, 5, 6, 7, 8, 9, 10, 0);
Console.WriteLine(number.Item9);
Console.WriteLine(number.Rest);
Console.WriteLine(number.Rest.Item1);

(string Name, char Gender, int Age) person2 = ("Ben", 'M', 40);
var person3 = (Name: "Bob", Gender: 'M', Age: 20);

string title = "C# Handbook";
int price = 500;
var book1 = (Title: title, Price: price);
var (Title, Price) = ("C# Cookbook", 900);
Console.WriteLine(book1);
Console.WriteLine((Title, Price));
Console.WriteLine($"Book: {Title}, Price:{Price}");

(int, double) x1 = (5, 3.14159);
(double First, double Second) x2 = (2.0, 1.0);
x2 = x1;
Console.WriteLine($"x2 = {x2.First}, {x2.Second}");

void ShowInfo((string Name, int Age, string Occupation) u)
{

}

ShowInfo(("Bob", 20, "Teacher"));

//Swap
var (x, y) = (3, 8);
Console.WriteLine($"x = {x}, y = {y}");
(x, y) = (y, x);
Console.WriteLine($"x = {x}, y = {y}");