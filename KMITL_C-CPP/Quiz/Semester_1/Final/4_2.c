#include <stdio.h>

int main() {
    double vec_list[4][4] = {
    {1.2, 3.1, 2.2, 1.3},
    {3.4, 1.6, 2.1, 3.2},
    {2.4, 1.1, 3.4, 1.4},
    {1.7}
    };

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%.2lf ", vec_list[i][j]);
        }
        printf("\n");
    }
    return 0;
}
