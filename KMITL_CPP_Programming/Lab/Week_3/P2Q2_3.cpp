#include <iostream>

using namespace std;

void print_tri2(char c, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            cout << c;
        }
        cout << endl;
    }
}

int main() {
    char usinChar;
    int height;
    cin >> usinChar >> height; // example: * 5
    print_tri2(usinChar, height);
}