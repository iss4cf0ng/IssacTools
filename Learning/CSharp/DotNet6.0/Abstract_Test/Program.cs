Rectangle rectangle = new Rectangle(2, 3);
Circle circle = new Circle(2);
Console.WriteLine(rectangle.Area());
Console.WriteLine(circle.Area());

public class Shape
{
   public virtual double Area()
    {
        return 0;
    }
}
public class Rectangle : Shape
{
    protected double Height { get; set; }
    protected double Width { get; set; }
    public Rectangle(double height, double width)
    {
        Height = height;
        Width = width;
    }
    public override double Area()
    {
        return Height * Width;
    }
}
public class Circle : Shape
{
    protected double R { get; set; }
    public Circle(double r)
    {
        R = r;
    }
    public override double Area()
    {
        return Math.PI * R * R;
    }
}