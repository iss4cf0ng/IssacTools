Cat cat = new Cat();
cat.Action();

public class Animal
{
    public void Action()
    {
        Console.WriteLine("Animal class Action");
        Moving();
    }
    public virtual void Moving()
    {
        Console.WriteLine("Animal can move.");
    }
}
public class Cat : Animal
{
    public override void Moving()
    {
        Console.WriteLine("Cat can move and jump.");
    }
}