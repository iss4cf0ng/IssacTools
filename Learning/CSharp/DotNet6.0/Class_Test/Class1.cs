namespace MyIntExtensionMethods
{
    public static class MyIntExtensions
    {
        public static bool IsLarger(this int i, int value)
        {
            return i > value;
        }
    }
}