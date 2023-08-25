using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using MyIntExtensionMethods;

ShadowTest A = new ShadowTest();
A.PrintInfo(20);
Console.WriteLine("Salary");
Salary sal = new Salary(10000);
sal.PrintInfo();

//Overload
Console.WriteLine("Overload");
Class_Overload_Constructor co = new Class_Overload_Constructor("20");

//Encapsulation
Console.WriteLine("Encapsulation");
Encapsulation_class enc = new Encapsulation_class();
enc.SetBalance(10000);
Console.WriteLine(enc.GetBalance());

//Balance
Console.WriteLine("Balance");
enc.Balance1 = 1000;
enc.Balance2 = 1000;
Console.WriteLine(enc.Balance1);
Console.WriteLine(enc.Balance2);

//Student
Student stu = new Student()
{
    Name = "ISSAC",
    Score = 0,
};


//Revenue
/*
Revenue p1 = new Revenue();
Console.Write("Enter revenue :");
int rev = Convert.ToInt32(Console.ReadLine());
p1.Money += rev;
p1.PrintInfo();
*/

//Extension Methods
int x = 10;
Console.WriteLine(x.IsLarger(20));

//Indexer
var my_score = new Score();
for (int i = 0; i < my_score.length; i++)
    Console.WriteLine($"Score {i} = {my_score[i]}");
my_score[1] = 58;
my_score[3] = 60;
for (int i = 0; i < my_score.length; i++)
    Console.WriteLine($"Score {i} = {my_score[i]}");

//Inhertance
Dog dog = new Dog("Lucky");
dog.Eat();
dog.Sleep();
dog.Barking();

class ShadowTest
{
    int x = 10;
    public void PrintInfo(int x)
    {
        Console.WriteLine(x);
        Console.WriteLine(this.x);
    }
}
class Salary
{
    int paid;
    public Salary(int paid) => this.paid = paid;
    public void PrintInfo()
    {
        Console.WriteLine($"salary : {this.paid}");
    }
}
class Class_Overload_Constructor
{
    public int age;
    public string name;
    public Class_Overload_Constructor(int age) => this.age = age;
    public Class_Overload_Constructor(string name) => this.name = name;
    public Class_Overload_Constructor(int age, string name)
    {
        this.age = age;
        this.name = name;
    }
}
class Encapsulation_class
{
    private int balance;
    public void SetBalance(int balance) => this.balance = balance;
    public int GetBalance() => this.balance;

    //Balance1 = Balance2
    public int Balance1
    {
        get => this.balance;
        set => this.balance = value;
    }

    public int Balance2 { get; set; }
}
class Student
{
    public int Score { get; set; } = 60;
    public string Name { get; set; } = "ISSAC";
    public void PrintInfo() => Console.WriteLine($"{Name} : {Score}");
}
class Point3D
{
    public int _x;
    public readonly int _y = 10;
    public readonly int _z;

    public Point3D(int x, int y, int z)
    {
        _x = x;
        _y = y;
        _z = z;
    }
}
class Revenue
{
    public static int _money;
    public int Money
    {
        get => _money;
        set => _money = value;
    }

    public void PrintInfo()
    {
        Console.WriteLine($"Total revenue : {_money}");
    }
}
class Score
{
    int[] sc = new int[5] { 80, 77, 96, 68, 91 };
    public int length => sc.Length;
    public int this[int index]
    {
        get => sc[index];
        set => sc[index] = value;
    }
}

class Animal
{
    protected string name;
    public Animal(string name) => this.name = name;

    public void Eat()
    {
        Console.WriteLine("Eating food.");
    }

    public void Sleep()
    {
        Console.WriteLine("Is sleeping.");
    }
}

class Dog : Animal
{
    public Dog(string name) : base(name) 
    {
        
    }

    public void Barking()
    {
        Console.WriteLine($"{name} is barking");
    }
}