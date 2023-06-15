#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

char* FileNameIn = "record.txt";
char* FileNameOut = "saved.txt";

int main()
{
    const int max_num = 40;
    const int max_size = 20;
    char Name [max_num][max_size];
    int Score[max_num];
    fstream FileInput(FileNameIn, ios::in);
    if (!FileInput) {
        cout << "File : " << FileNameIn << "open failed!" << endl;
        exit(1);
    }
    fstream FileOutput(FileNameOut, ios::out);
    if (!FileOutput) {
        cout << "File : " << FileNameOut << "save failed!" << endl;
        exit(1);
    }
    int count = 0;
    while (FileInput.peek() != EOF && (count < max_num)) {
        FileInput >> Name[count] >> Score[count];
        count++;
    }

    for (int i = 0; i < count; i++) {
        Score[i] = Score[i] * 0.8 + 20;
        FileOutput << "(" << i + 1 << ")"
            << setw(12) << Name[i] << " "
            << setw(5) << Score[i] << endl;
    }
    FileOutput.close();
    FileInput.close();
    cout << "Save file at : " << FileNameOut << endl;
    
    system("pause");
    return 0;
}