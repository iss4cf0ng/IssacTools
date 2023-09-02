School A = new School();
School B = new Department();
A.Demo();
B.Demo();

public class School
{
    public virtual void Demo()
    {
        Console.WriteLine("Demo1");
    }
}
public class Department : School
{
    public override void Demo()
    {
        Console.WriteLine("Demo2");
    }
}