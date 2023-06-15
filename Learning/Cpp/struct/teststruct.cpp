#include <iostream>
using namespace std;

struct Employee
{
    char Name[20];
    char Phone[10];
    int Id;
};

int main()
{
    Employee Ea = {"Peter", "123", 1};
    Employee Eb = {"Ben", "456", 2};
}