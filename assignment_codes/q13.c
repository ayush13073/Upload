#include <stdio.h>

int main() {
    int r, c;
    scanf("%d %d", &r, &c);
    int A[r][c], B[r][c], Sum[r][c], Transpose[c][r];

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            scanf("%d", &A[i][j]);

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            scanf("%d", &B[i][j]);

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            Sum[i][j] = A[i][j] + B[i][j];

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            Transpose[j][i] = A[i][j];

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) printf("%d ", Sum[i][j]);
        printf("\n");
    }

    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) printf("%d ", Transpose[i][j]);
        printf("\n");
    }
    return 0;
}
