DataPair<string, int> noodle = new DataPair<string, int>();
noodle.Key = "Beef";
noodle.Value = 180;
Console.WriteLine($"{noodle.Key} : {noodle.Value}");

DataBank<int> x = new DataBank<int>();
x.AddItem(0, 5);
x.AddItem(2, 6);
x.AddItem(4, 7);
for (int i = 0; i < 6; i++)
    Console.WriteLine($"arr[{i}] = {x.GetArr(i)}");

public class DataPair<TKey, TValue>
{
    public TKey? Key { get; set; }
    public TValue? Value { get; set; }
}

public class DataBank<T>
{
    public T[] arr = new T[5];
    public void AddItem(int index, T item)
    {
        arr[index] = item;
    }
    public T GetArr(int index)
    {
        if (index >= 0 && index < arr.Length)
            return arr[index];
        else
            return default(T);
    }
} 