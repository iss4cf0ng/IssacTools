#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    char *FileNameIn = "input.txt";
    char *FileNameOut = "output.txt";
    double input, text;
    ifstream FileInput;
    ofstream FileOutput;
    FileInput.open(FileNameIn);
    FileOutput.open(FileNameOut);

    if (!FileInput)
    {
        cout << "Open file: " << FileNameIn
            << "failed!" << endl; exit(1);
    }

    if (!FileOutput)
    {
        cout << "Save file: " << FileNameOut
            << "failed!" << endl; exit(1);
    }

    FileInput >> input;
    
}