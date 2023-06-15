#include <iostream>
using namespace std;
#include "First.h"
#include "Second.h"

int main()
{
    NS1::Member Ma = {"Geo", 2323232};
    NS2::Member Mb = {34, "AAA", 1212.21};
    cout << "Name of Ma is : " << Ma.Name << endl;
    cout << "Name of Mb is : " << Mb.Name << endl;
    cout << "NS1::Gain is : " << NS1::Gain << endl;
    cout << "NS2::Gain is : " << NS2::Gain << endl;
    cout << "NS1::Fnc(2.5) : " << NS1::Fnc(2.5) << endl;
    cout << "NS2::Fnc(2.5) : " << NS2::Fnc(2.5) << endl;
    system("pause");
    return 0;
}