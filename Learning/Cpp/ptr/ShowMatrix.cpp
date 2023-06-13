#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    const int row = 2;
    const int col = 3;
    double B[row][col] = {1.8, 4.9, 6.8, 6.2, 2.1, 3.4};
    int i, j;

    cout << "(1)Array B:" << endl;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
            cout << setw(5) << B[i][j];
        cout << endl;
    }
    cout << endl;

    cout << "(2)Array B:" << endl;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
            cout << setw(5) << *(B[i] + j);
        cout << endl;
    }
    cout << endl;

    cout << "(3)Array B:" << endl;
    for (i = 0; i < col; i++)
    {
        for (j = 0; j < col; j++)
            cout << setw(5) << *(*(B + i) + j);
        cout << endl;
    }
    cout << endl;

    system("pause");
    return 0;
}