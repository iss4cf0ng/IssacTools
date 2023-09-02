static string UpperString(string input) => input.ToUpper();

Func<string, string> convert_brand = UpperString; //(string input) => input.ToUpper();
string brand = "bmw";
Console.WriteLine(convert_brand(brand));