#include <iostream>
#include <iomanip>
using namespace std;

inline double C2F(double C)
{ return C*9/5 + 32; }

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