#include <iostream>
using namespace std;

const int Size = 5;
double Average(double *);
double MaxElem(double *);
int main()
{
    double P[Size] = {48.4, 39.8, 40.5, 42.6, 41.2};
    cout << "Average of P : " << Average(P) << endl;
    cout << "Maximum of P : " << MaxElem(P) << endl;
    system("pause");
    return 0;
}

double Average(double* V)
{
    double sum = 0;
    for (int i = 0; i < Size; i++)
        sum += *(V + i);
    return sum / Size;
}

double MaxElem(double* V)
{
    double MaxE;
    MaxE = V[0];
    for (int i = 1; i < Size; i++)
        if (MaxE < V[i]) MaxE = V[i];
    return MaxE;
}