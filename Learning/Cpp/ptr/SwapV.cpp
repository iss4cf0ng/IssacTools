#include <iostream>
#include <iomanip>
using namespace std;

void DisplayV1(double *, int);
void DisplayV2(double *, int);
void Swap(double **, double **);
int main()
{
    const int SizeA = 5;
    const int SizeB = 7;
    double* A = new double[SizeA];
    double* B = new double[SizeB];
    for (int i = 0; i < SizeA; i++) A[i] = 1.0*i;
    for (int j = 0; j < SizeB; j++) B[j] = 3.0*j;

    cout << "Before Swap() " << endl;
    cout << "A : \n";
    DisplayV1(A, SizeA);
    cout << "B : \n";
    DisplayV2(B, SizeB);

    Swap(&A, &B);
    cout << "After Swap() : \n";
    cout << "A : \n";
    DisplayV1(A, SizeA);
    cout << "B : \n";
    DisplayV2(B, SizeB);

    delete [] A;
    delete [] B;
    system("pause");
    return 0;
}

void DisplayV1(double* V, int N)
{
    cout << endl;
    for (int i = 0; i < N; i++)
        cout << setw(5) << V[i] << " ";
    cout << endl;
    return;
}

void DisplayV2(double* V, int N)
{
    cout << endl;
    for (int i = 0; i < N; i++)
        cout << setw(5) << *(V+i) << " ";
    cout << endl;
    return;
}

void Swap(double ** x, double ** y)
{
    double * temp;
    temp = *x;
    *x = *y;
    *y = temp;
    return;
}