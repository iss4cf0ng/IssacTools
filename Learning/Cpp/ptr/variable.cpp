#include <iostream>
using namespace std;

int main()
{
    double A = 2.5;
    cout << "A : " << A << endl;
    cout << "A size : " << sizeof(A) << endl;
    cout << "\tor sizeof(double) : " << sizeof(double) << endl;
    cout << "Address of A : " << &A << endl;
    system("pause");
    return 0;
}