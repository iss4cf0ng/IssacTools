#include <iostream>
using namespace std;

int main()
{
    char str1[30] = "Hello here is the test";
    char *ptr_str1 = str1;

    cout << "---Same result---" << endl;
    cout << str1 << endl;
    cout << ptr_str1 << endl;
    cout << "---String ptr---" << endl;
    
}