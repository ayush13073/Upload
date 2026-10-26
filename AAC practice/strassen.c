#include <stdio.h>

#define MAX 16

void add(int n, int A[MAX][MAX], int B[MAX][MAX], int C[MAX][MAX]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
}

void subtract(int n, int A[MAX][MAX], int B[MAX][MAX], int C[MAX][MAX]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
}

void strassen(int n, int A[MAX][MAX], int B[MAX][MAX], int C[MAX][MAX]) {
    if (n == 1) {
        C[0][0] = A[0][0] * B[0][0];
        return;
    }

    if (n == 2) {
        int m1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1]);
        int m2 = (A[1][0] + A[1][1]) * B[0][0];
        int m3 = A[0][0] * (B[0][1] - B[1][1]);
        int m4 = A[1][1] * (B[1][0] - B[0][0]);
        int m5 = (A[0][0] + A[0][1]) * B[1][1];
        int m6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1]);
        int m7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1]);

        C[0][0] = m1 + m4 - m5 + m7;
        C[0][1] = m3 + m5;
        C[1][0] = m2 + m4;
        C[1][1] = m1 - m2 + m3 + m6;
        return;
    }

    int k = n / 2;
    int a11[MAX][MAX], a12[MAX][MAX], a21[MAX][MAX], a22[MAX][MAX];
    int b11[MAX][MAX], b12[MAX][MAX], b21[MAX][MAX], b22[MAX][MAX];
    int c11[MAX][MAX], c12[MAX][MAX], c21[MAX][MAX], c22[MAX][MAX];
    int m1[MAX][MAX], m2[MAX][MAX], m3[MAX][MAX], m4[MAX][MAX], m5[MAX][MAX], m6[MAX][MAX], m7[MAX][MAX];
    int t1[MAX][MAX], t2[MAX][MAX];

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            a11[i][j] = A[i][j];
            a12[i][j] = A[i][j + k];
            a21[i][j] = A[i + k][j];
            a22[i][j] = A[i + k][j + k];

            b11[i][j] = B[i][j];
            b12[i][j] = B[i][j + k];
            b21[i][j] = B[i + k][j];
            b22[i][j] = B[i + k][j + k];
        }
    }

    // M1 = (A11 + A22) * (B11 + B22)
    add(k, a11, a22, t1);
    add(k, b11, b22, t2);
    strassen(k, t1, t2, m1);

    // M2 = (A21 + A22) * B11
    add(k, a21, a22, t1);
    strassen(k, t1, b11, m2);

    // M3 = A11 * (B12 - B22)
    subtract(k, b12, b22, t2);
    strassen(k, a11, t2, m3);

    // M4 = A22 * (B21 - B11)
    subtract(k, b21, b11, t2);
    strassen(k, a22, t2, m4);

    // M5 = (A11 + A12) * B22
    add(k, a11, a12, t1);
    strassen(k, t1, b22, m5);

    // M6 = (A21 - A11) * (B11 + B12)
    subtract(k, a21, a11, t1);
    add(k, b11, b12, t2);
    strassen(k, t1, t2, m6);

    // M7 = (A12 - A22) * (B21 + B22)
    subtract(k, a12, a22, t1);
    add(k, b21, b22, t2);
    strassen(k, t1, t2, m7);

    // C11 = M1 + M4 - M5 + M7
    add(k, m1, m4, t1);
    subtract(k, t1, m5, t2);
    add(k, t2, m7, c11);

    // C12 = M3 + M5
    add(k, m3, m5, c12);

    // C21 = M2 + M4
    add(k, m2, m4, c21);

    // C22 = M1 - M2 + M3 + M6
    subtract(k, m1, m2, t1);
    add(k, t1, m3, t2);
    add(k, t2, m6, c22);

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            C[i][j] = c11[i][j];
            C[i][j + k] = c12[i][j];
            C[i + k][j] = c21[i][j];
            C[i + k][j + k] = c22[i][j];
        }
    }
}

int main(void) {
    int n;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    /*
     * INPUT INSTRUCTIONS:
     * 1. Enter n (dimension of matrix, should be a power of 2: 2, 4, etc.).
     * 2. Enter n x n elements of Matrix A row by row.
     * 3. Enter n x n elements of Matrix B row by row.
     */

    printf("STRASSEN'S MATRIX MULTIPLICATION\n");
    printf("Enter dimension n (power of 2, e.g., 2 or 4): ");
    scanf("%d", &n);

    printf("Enter elements of Matrix A (%d x %d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Enter elements of Matrix B (%d x %d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    strassen(n, A, B, C);

    printf("\nResultant Matrix C (A * B):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%6d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}