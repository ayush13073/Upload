#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_NUM 20

int board[MAX_NUM];
int solution_count = 0;

void printqueen(int n) {
    printf("Solution #%d:\n", ++solution_count);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (board[i] == j) {
                printf(" Q ");
            } else {
                printf(" . ");
            }
        }
        printf("\n");
    }
    printf("\n");
}

bool issafe(int k, int col) {
    for (int i = 1; i < k; i++) {
        if (board[i] == col || abs(board[i] - col) == abs(i - k)) {
            return false;
        }
    }
    return true;
}

void nqueen(int k, int n) {
    for (int col = 1; col <= n; col++) {
        if (issafe(k, col)) {
            board[k] = col;

            if (k == n) {
                printqueen(n);
            } else {
                nqueen(k + 1, n);
            }
        }
    }
}

int main(void) {
    int n;

    printf("N-QUEENS PROBLEM (BACKTRACKING)\n");
    printf("Enter the number of queens (1 to %d): ", MAX_NUM - 1);

    // Validate integer input within valid bounds
    if (scanf("%d", &n) != 1 || n < 1 || n >= MAX_NUM) {
        printf("Error: Invalid input! Please enter an integer between 1 and %d.\n", MAX_NUM - 1);
        return 1;
    }

    nqueen(1, n);

    if (solution_count == 0) {
        printf("No solution exists for N = %d.\n", n);
    } else {
        printf("Total solutions found: %d\n", solution_count);
    }

    return 0;
}