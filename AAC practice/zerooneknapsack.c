#include <stdio.h>

#define MAX_ITEMS 100
#define MAX_CAPACITY 1000

// Helper function to find maximum of two values
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Function to solve 0/1 Knapsack using Dynamic Programming
void knapsack01(int n, int W, int weights[], int values[]) {
    int dp[MAX_ITEMS + 1][MAX_CAPACITY + 1];

    // Build DP table in bottom-up manner
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (weights[i - 1] <= w) {
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // Maximum achievable value is stored at dp[n][W]
    printf("\nMaximum value achievable: %d\n", dp[n][W]);

    // Backtrack to identify which items are included in the optimal set
    printf("Items selected (1-indexed):\n");
    int w = W;
    for (int i = n; i > 0 && dp[i][w] > 0; i--) {
        // If the value differs from the cell directly above, item (i-1) was included
        if (dp[i][w] != dp[i - 1][w]) {
            printf("Item %d (Weight: %d, Value: %d)\n", i, weights[i - 1], values[i - 1]);
            w -= weights[i - 1]; // Deduct weight of the chosen item
        }
    }
}

int main(void) {
    int n, W;
    int weights[MAX_ITEMS], values[MAX_ITEMS];

    /*
     * INPUT INSTRUCTIONS:
     * 1. Enter number of items (n).
     * 2. Enter maximum knapsack capacity (W).
     * 3. Enter weights of the n items separated by spaces.
     * 4. Enter corresponding values/profits of the n items separated by spaces.
     */

    printf("0/1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING)\n");
    printf("Enter number of items: ");
    scanf("%d", &n);

    printf("Enter maximum knapsack capacity: ");
    scanf("%d", &W);

    printf("Enter weights of %d items: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &weights[i]);
    }

    printf("Enter values of %d items: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &values[i]);
    }

    knapsack01(n, W, weights, values);

    return 0;
}