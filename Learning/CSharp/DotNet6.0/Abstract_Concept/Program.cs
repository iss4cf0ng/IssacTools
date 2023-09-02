Rectangle rectangle = new Rectangle();
Circle circle = new Circle();
rectangle.Draw();
circle.Draw();

Bmw bmw = new Bmw("Peter");
bmw.Refuel();
bmw.Run();

abstract class Shape
{
    abstract public void Draw();
}
class Rectangle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Draw rectangle.");
    }
}
class Circle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Draw circle.");
    }
}

public abstract class Car
{
    public abstract string Name { get; } //abstract property, get = readonly
    public abstract void Run();
    public void Refuel()
    {
        Console.WriteLine($"{Name} refuel.");
    }
}
public class Bmw : Car
{
    private string name; //Define name
    public Bmw(string name) //Constructor
    {
        this.name = name;
    }
    public override void Run()
    {
        Console.WriteLine("Save driving...");
    }
    public override string Name
    {
        get { return this.name + " traveling"; }
    }
}