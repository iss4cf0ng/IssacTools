Cat cat = new Cat("Lucy", "fish");
cat.Eat();
cat.Like();
cat.Jumping();

//base test
Child ch = new Child();
ch.PrintInfo();

//IS-A (is a kind of)
Console.WriteLine(cat is Animal);
Console.WriteLine(cat is Cat);

//HAS-A (Aggregation)
Circle circle = new Circle();
double area = circle.GetArea(10);
Console.WriteLine(area);

//HAS-A Combination
Sentra sentra = new Sentra();
sentra.SetMaxSpeed(100);
sentra.SetColor("Blue");
sentra.PrintCarInfo();
sentra.SentraShow();

public class Animal
{
    protected string Name { get; set; } = string.Empty;
    public void Eat()
    {
        Console.WriteLine($"{Name} is eating.");
    }
}
public class Mammal : Animal
{
    protected string FavoriteFood { get; set; } = string.Empty;
    public Mammal(string name)
    {
        Name = name;
    }
    public void Like()
    {
        Console.WriteLine($"{Name} like to eat {FavoriteFood}");
    }
}
public class Cat : Mammal
{
    public Cat(string name, string favorite_food) : base(name)
    {
        FavoriteFood = favorite_food;
    }
    public void Jumping()
    {
        Console.WriteLine($"{Name} is jumping.");
    }
}

class Father
{
    public int x = 50;
}
class Child : Father
{
    public int x = 100;
    public void PrintInfo()
    {
        Console.WriteLine($"Father x = {base.x}");
        Console.WriteLine($"Child x = {x}");
    }
}

//Aggregation
public class MyMath
{
    public double Square(double x)
    {
        return x * x;
    }
}
public class Circle
{
    public MyMath math;
    public double GetArea(double radius)
    {
        math = new MyMath();
        double r_square = math.Square(radius);
        return r_square * Math.PI;
    }
}

public class Car
{
    int max_speed;
    string color;
    //Set maximum speed
    public void SetMaxSpeed(int max_speed) => this.max_speed = max_speed;
    //Set car color
    public void SetColor(string color) => this.color = color;
    public void PrintCarInfo()
    {
        Console.WriteLine($"Car max speed : {max_speed}\nColor : {color}");
    }
}
public class Engine
{
    public void Starting() => Console.WriteLine("Engine start");
    public void Running() => Console.WriteLine("Engine is running");
    public void Stoping() => Console.WriteLine("Engine stop");
}
public class Sentra : Car
{
    public void SentraShow()
    {
        Engine engine = new Engine();
        engine.Starting();
        engine.Running();
        engine.Stoping();
    }
}