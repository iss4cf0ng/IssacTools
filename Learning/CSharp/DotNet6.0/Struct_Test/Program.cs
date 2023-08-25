Coordinate coord = new Coordinate();
coord.x = 3;
coord.y = 4;
Console.WriteLine(coord.x);
coord = new Coordinate(1, 3);
Console.WriteLine(coord.x);

//Readonly, with
Console.WriteLine("Readonly, with");
var p1 = new Coords(2, 5);
Console.WriteLine($"({p1.X}, {p1.Y})");
var p2 = p1 with { X = 3 };
Console.WriteLine($"({p2.X}, {p2.Y})");
struct Coordinate
{
    public int x;
    public int y;

    public Coordinate(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}

struct Student
{
    private int id;
    private string name;
    public int ID
    {
        get { return id; }
        set { id = value; }
    }

    public string Name
    {
        get { return name; }
        set { name = value; }
    }
}

readonly struct Coords
{
    public Coords(double x, double y)
    {
        X = x;
        Y = y;
    }

    public double X { get; init; }
    public double Y { get; init; }
}