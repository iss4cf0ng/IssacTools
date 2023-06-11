#include <iostream>
using namespace std;

void Swap(int&, int&);
int main()
{
    int A = 10, B = 5;
    Swap(A, B);
    cout << "A : " << A << endl;
    cout << "B : " << B << endl;
}

void Swap(int &x, int &y) 
{
    int temp;
    temp = x;
    x = y;
    y = temp;
}