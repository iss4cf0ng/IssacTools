Dog dog = new Dog();
dog.Action();

John john = new John();
john.GrandfatherMethod();
john.FatherMethod();



interface IAnimal
{
    void Action();
}
class Dog : IAnimal
{
    public void Action()
    {
        Console.WriteLine("Dog : is running.");
    }
}

interface IGrandfather
{
    void GrandfatherMethod();
}
interface IFather : IGrandfather
{
    void FatherMethod();
}
class John : IFather
{
    public void GrandfatherMethod()
    {
        Console.WriteLine("Call GrandFatherMethod");
    }
    public void FatherMethod()
    {
        Console.WriteLine("Call FatherMethod");
    }
}

interface IComputer
{
    void Office();
    void Programming(string text);
}
class Software : IComputer
{
    void IComputer.Office() { Console.WriteLine("Common staff"); }
    void IComputer.Programming(string text) { Console.WriteLine("Programming."); }
    public void Web(string text) { Console.WriteLine("Web design."); }
}

interface ICoord
{
    int X { get; set; }
    int Y { get; set; }
    double Distance { get; }
}
class Point : ICoord
{
    public int X { get; set; }
    public int Y { get; set; }
    public double Distance => Math.Sqrt(X * X + Y * Y);
    public Point(int x, int y)
    {
        
    }
}