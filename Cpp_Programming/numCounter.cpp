#include <iostream>
int main() {
    int userNumber;

    std::cout << "Enter a positive number: ";
    std::cin >> userNumber;

    if (userNumber <= 0) {
        std::cout << "That is not positive!\n";
    } else {
        std::cout << "Counting up to " << userNumber << ":\n";
        for (int i = 1; i <= userNumber; i++) {
            std::cout << i << " ";
        }
        std::cout << "\n";
    }

    return 0;
}
