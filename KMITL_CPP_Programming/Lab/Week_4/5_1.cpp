#include <iostream>

using namespace std;

int main() {
    FILE* file = fopen("5_1.txt", "r");
    for (int c; (c = fgetc(file)) != EOF;) {
        putchar(toupper(c));
    }
    fclose(file);
}