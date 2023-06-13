#include <iostream>
using namespace std;

int main()
{
    const int size = 5;
    double V[size] = {48.5, 39.8, 40.5, 42.6, 41.2};
    double sum = 0.0;
    double *pV = V;
    int i;
    for (i = 0; i < size; i++)
    {
        cout << "Element : " << *pV << endl;
        sum += *pV++;
    }
    cout << "Total elements sum : " << sum << endl;
    cout << "Average of elements : " << sum / size << endl;

    //Another
    sum = 0.0;
    pV = V;
    while (pV < V + size)
        sum += *pV++;
    cout << "Total elements sum : " << sum << endl;
    cout << "Average of elements : " << sum / size << endl;

    system("pause");
    return 0;
}