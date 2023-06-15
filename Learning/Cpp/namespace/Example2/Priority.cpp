#include <iostream>
using namespace std;

namespace NS
{
    int M = 10;
    float x = 1.0, y = 2.0;
    char C = 'G';
}

int main()
{
    NS::M = 6;
    {
        float y = 7.5;
        using namespace NS;
        x = 5.6;
        cout << y;
    }
    system("pause");
    return 0;
}