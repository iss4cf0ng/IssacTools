#include <iostream>
#include <iomanip>
using namespace std;

double C2F(double C)
{
    double F;
    F = C*9/5 + 32;
    return F;
}

int main()
{
    double CTemp;
    cout << " C  F" << endl;
    cout << "------" << endl;
    for (int i = 1; i <= 10; i++)
    {
        CTemp = 10*i;
        cout << setw(5) << CTemp << " " 
            << setw(5) << C2F(CTemp) << endl;
    }
    cout << "------" << endl;
    system("pause");
    return 0;
}