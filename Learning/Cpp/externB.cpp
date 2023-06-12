int Bp;
extern int Am;

void Func1()
{
    Bp = 2;
    Am = 8;
}

void Func2()
{
    extern int An;
    Am += 10;
    An = 27;
}