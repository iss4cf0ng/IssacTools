#include <iostream>
using namespace std;

int Am, An;
static int ASx, ASy;

void Func1(), Func2(), Func3();
int main()
{
    cout << "Executed Func1() \n";
    Func1();
    cout << "Am value : " << Am << endl;
    cout << "An value : " << An << endl;
    cout << endl;
    cout << "Executed Func2() \n";
    Func2();

}
extern int Bp;

void Func3()
{
    cout << "Bp value : " << Bp << endl;
    cout << endl;
}