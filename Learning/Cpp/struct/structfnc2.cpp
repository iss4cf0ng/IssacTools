#include <iostream>
#include <cstring>
using namespace std;

struct Employee
{
    char Name[20];
    char Phone[10];
    int Id;
};

void ShowMember(Employee A)
{
    cout << "Data information : " << endl
        << "Name : " << A.Name << endl
        << "Phone : " << A.Phone << endl
        << "Id : " << A.Id << endl;
}

void ChangeName(Employee& A, char NewName[])
{
    strcpy(A.Name, NewName);
}

void ChangeId(Employee* pE, int NewId)
{
    pE -> Id = NewId;
}

int main()
{
    Employee Ea = {"Ann", "123", 105};
    Employee Eb = {"Ben", "456", 110};
    ShowMember(Ea);
    ShowMember(Eb);
    ChangeId(&Ea, 208);
    cout << "After ChangeId() : " << endl;
    ShowMember(Ea);
    system("pause");
    return 0;
}