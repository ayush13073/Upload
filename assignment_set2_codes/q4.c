#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool isSafe(int board[], int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col || abs(board[i] - col) == abs(i - row)) {
            return false;
        }
    }
    return true;
}

void printBoard(int board[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i] == j) printf("Q ");
            else printf(". ");
        }
        printf("\n");
    }
    printf("\n");
}

void solveNQueens(int board[], int row, int n) {
    if (row == n) {
        printBoard(board, n);
        return;
    }
    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col)) {
            board[row] = col;
            solveNQueens(board, row + 1, n);
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int board[n];
    solveNQueens(board, 0, n);
    return 0;
}
