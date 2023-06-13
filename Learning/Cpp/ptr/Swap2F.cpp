#include <iostream>
using namespace std;

void SwapF(double* x, double* y);
int main()
{
    double a = 2;
    double b = 5;
    cout << "Before SwapF()\n";
    cout << "a : " << a << " b : " << b << endl;
    SwapF(&a, &b);
    cout << "After SwapF()\n";
    cout << "a : " << a << " b : " << b << endl;
    system("pause");
    return 0;
}

void SwapF(double* x, double* y)
{
    double temp;
    temp = *x;
    *x = *y;
    *y = temp;
}