#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream file("/data.txt");
    std::string word;
    std::string line;

    // Reads line by line until End-Of-File (EOF)
    while (std::getline(file, line))
    {
        std::cout << line << "\n";
    }

        // Open a file for writing (creates file if it doesn't exist)
        std::ofstream outFile("output.txt");

        if (outFile.is_open())
        {
            outFile << "Student Name: John Doe\n";
            outFile << "Score: " << 95.5 << "\n";

            outFile.close(); // Close the file stream
            std::cout << "Data saved successfully!\n";
        }
        else
        {
            std::cerr << "Error opening file!\n";
        }

    /*
    // Open the file in append mode (std::ios::app)
    std::ofstream outFile("output.txt", std::ios::app);

    if (outFile.is_open())
    {
        // This text will be added at the end of output.txt
        outFile << "New log entry added at the end.\n";
        outFile << "Score: 100\n";

        outFile.close(); // Close the file stream
        std::cout << "Data appended successfully!" << std::endl;
    }
    else
    {
        std::cerr << "Error opening file for appending!" << std::endl;
    }
*/
    return 0;
}