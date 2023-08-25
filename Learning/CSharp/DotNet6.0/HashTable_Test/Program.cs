using System.Collections;

Hashtable ht = new()
{
    {"Sunday", "星期日" },
    {"Monday", "星期一" }
};
Console.WriteLine(ht["Sunday"]);
foreach (object k in ht.Keys)
    Console.WriteLine(ht[k]);