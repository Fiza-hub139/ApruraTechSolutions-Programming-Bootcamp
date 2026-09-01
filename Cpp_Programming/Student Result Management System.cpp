#include <iostream>
#include <fstream>
using namespace std;

// Structure 
struct Student {
    string name;
    int math, english, cs;
    int total;
    float percentage;
    char grade;
};

// function declarations
void inputStudent(Student s[], int size);
void calculate(Student s[], int size);
void display(Student s[], int size);
void saveToFile(Student s[], int size);
int findTopper(Student s[], int size);

//  Main function
int main() {
    int size;

    cout << "Enter number of students: ";
    cin >> size;

    Student s[50];

    inputStudent(s, size);
    calculate(s, size);
    display(s, size);

    saveToFile(s, size);

    int topIndex = findTopper(s, size);
    cout << "\n TOPPER: " << s[topIndex].name
         << " (" << s[topIndex].total << " marks)\n";

    return 0;
}

//  Input Function
void inputStudent(Student s[], int size) {
    for (int i = 0; i < size; i++) {
        cout << "\nEnter name of student " << i + 1 << ": ";
        cin >> s[i].name;

        cout << "Enter Math marks: ";
        cin >> s[i].math;

        cout << "Enter English marks: ";
        cin >> s[i].english;

        cout << "Enter CS marks: ";
        cin >> s[i].cs;
    }
}

//  Calculation Function 
void calculate(Student s[], int size) {
    for (int i = 0; i < size; i++) {

        s[i].total = s[i].math + s[i].english + s[i].cs;
        s[i].percentage = s[i].total / 3.0;

        // Grade System
        if (s[i].percentage >= 80)
            s[i].grade = 'A';
        else if (s[i].percentage >= 60)
            s[i].grade = 'B';
        else
            s[i].grade = 'C';
    }
}

//  Display Function 
void display(Student s[], int size) {
    cout << "\n----- RESULT SHEET -----\n";

    for (int i = 0; i < size; i++) {
        cout << "\nName: " << s[i].name;
        cout << "\nMath: " << s[i].math;
        cout << "\nEnglish: " << s[i].english;
        cout << "\nCS: " << s[i].cs;
        cout << "\nTotal: " << s[i].total;
        cout << "\nPercentage: " << s[i].percentage;
        cout << "\nGrade: " << s[i].grade;

        if (s[i].percentage >= 50)
            cout << "\nResult: PASS\n";
        else
            cout << "\nResult: FAIL\n";

        cout << "----------------------";
    }
}

// File Storage 
void saveToFile(Student s[], int size) {
    ofstream file("students.txt");

    file << "STUDENT RESULT RECORD\n\n";

    for (int i = 0; i < size; i++) {
        file << "Name: " << s[i].name << endl;
        file << "Math: " << s[i].math << endl;
        file << "English: " << s[i].english << endl;
        file << "CS: " << s[i].cs << endl;
        file << "Total: " << s[i].total << endl;
        file << "Percentage: " << s[i].percentage << endl;
        file << "Grade: " << s[i].grade << endl;
        file << "------------------------\n";
    }

    file.close();

    cout << "\n Data saved to file successfully!\n";
}

//  Topper Function 
int findTopper(Student s[], int size) {
    int topIndex = 0;

    for (int i = 1; i < size; i++) {
        if (s[i].total > s[topIndex].total) {
            topIndex = i;
        }
    }

    return topIndex;
}
