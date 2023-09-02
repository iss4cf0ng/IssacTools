static void EventHandler() => Console.WriteLine("EventA handle finished");

Publisher obj = new Publisher();
obj.EventA += EventHandler;
obj.StartEventA();

public delegate void Notify();
public class Publisher
{
    public event Notify EventA;
    public void StartEventA()
    {
        Console.WriteLine("EventA happen");
    }
    protected virtual void EventAHappen()
    {
        EventA?.Invoke();
    }
}