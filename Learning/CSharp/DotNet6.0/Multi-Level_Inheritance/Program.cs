Cat cat = new Cat("Lucy", "fish");
cat.Eat();
cat.Like();
cat.Jumping();

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