int[] arr = new int[] { 1, 2, 5, 11, 21, 12, 6, 9, 20 };
var query1 = from n in arr select n;
foreach (var q in query1)
    Console.Write($"{q}, ");
Console.WriteLine();

//where
arr = new int[] { 1, 3, 5, 11, 21, 12, 6, 9, 20 };
var query2 = from n in arr
             where n < 10
             select n;
foreach (var q in query2)
    Console.Write($"{q}, ");
Console.WriteLine();

var students = new List<Student>()
{
    new Student() { Id = 1, Name = "Ben", Major = "CS"},
    new Student() { Id = 2, Name = "Peter", Major = "EE"},
    new Student() { Id = 3, Name = "Bob", Major = "Math"},
};
var query3 = from student in students
             where student.Major == "CS"
             select student;
foreach (var q in query3)
    Console.WriteLine($"{q.Id}, {q.Name}");
Console.WriteLine();

//let
string[] news =
{
    "Apple introduced Safety Check.",
    "This robust security setting.",
    "You may stop sharing your information.",
};
var query4 =
    from sentence in news
    let words = sentence.Split(' ')
    from word in words
    let w = word.ToLower()
    where w[0] == 'a' || w[0] == 'i' || w[0] == 't'
    select word;
foreach (var q in query4)
    Console.Write($"{q}, ");
Console.WriteLine();

//orderby
arr = new int[] { 8, 3, 5, 11, 21, 12, 6, 9, 20 };
var query5 = from n in arr
             where n < 10
             orderby n
             select n;
foreach (var q in query5)
    Console.Write($"{q}, ");
Console.WriteLine();

var query6 = from n in arr
             where n < 10
             orderby n descending
             select n;
foreach (var q in query6)
    Console.Write($"{q}, ");
Console.WriteLine();
Console.WriteLine();

//group...by
arr = new int[] { 8, 3, 5, 11, 21, 12, 6, 9, 20 };
var query7 = from n in arr
             where n < 10
             group n by (n % 2);
foreach (var q in query7)
    foreach (var element in q)
        Console.Write($"{element}, ");
    Console.WriteLine();
Console.WriteLine();

//group...by/into
students = new List<Student>()
{
    new Student() { Id = 1, Name = "Ben", Major = "CS"},
    new Student() { Id = 2, Name = "Peter", Major = "EE"},
    new Student() { Id = 3, Name = "Bob", Major = "Math"},
    new Student() { Id = 4, Name = "Curry", Major = "EE"},
    new Student() { Id = 5, Name = "Macro", Major = "CS"},
};
var query8 = from student in students
             group student by student.Major into NewGroup
             select NewGroup;
foreach (var q_group in query8)
{
    Console.WriteLine($"Major : {q_group.Key}");
    foreach (var student in q_group)
        Console.WriteLine($"\t{student.Id}, {student.Name}");
}

//join
int[] outer = new int[] { 1, 2, 3, 4, 5, 6, 7 };
int[] inner = new int[] { 1, 3, 4, 7 };
var query9 = from a in outer
             join b in inner
             on a equals b
             where b > 1
             select b;
Console.WriteLine("Item:");
foreach (var item in query9)
    Console.Write($"{item}, ");

public class Student
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Major { get; set; }
}