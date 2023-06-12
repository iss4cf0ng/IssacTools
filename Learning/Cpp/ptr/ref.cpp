#include <iostream>
using namespace std;

int main()
{
    double x = 1.0;
    double &y = x;
    double *p = &x;

    cout << "Original x : " << x << endl;
    *p = 5.0;
    cout << "New x : " << x << endl;
}