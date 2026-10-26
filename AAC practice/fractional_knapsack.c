#include <stdio.h>

#define MAX_ITEMS 100

void fractionalKnapsack(int n, float capacity, float weights[], float profits[]) {
    float ratio[MAX_ITEMS];
    float solution[MAX_ITEMS];
    float totalprofit = 0.0;
    float currentCapacity = capacity;

    for (int i = 0; i < n; i++) {
        ratio[i] = profits[i] / weights[i];
        solution[i] = 0.0;
    }

    // Sort items by profit/weight ratio in descending order
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (ratio[j] < ratio[j + 1]) {
                float tempratio = ratio[j];
                ratio[j] = ratio[j + 1];
                ratio[j + 1] = tempratio;

                float tempweight = weights[j];
                weights[j] = weights[j + 1];
                weights[j + 1] = tempweight;

                float tempprofit = profits[j];
                profits[j] = profits[j + 1];
                profits[j + 1] = tempprofit;
            }
        }
    }

    // Greedy selection
    for (int i = 0; i < n; i++) {
        if (weights[i] <= currentCapacity) {
            solution[i] = 1.0;
            totalprofit += profits[i];
            currentCapacity -= weights[i];
        } else {
            solution[i] = currentCapacity / weights[i];
            totalprofit += solution[i] * profits[i];
            currentCapacity = 0.0;
            break;
        }
    }

    printf("\nFraction of each item taken:\n");
    for (int i = 0; i < n; i++) {
        printf("Item with weight %.2f and profit %.2f : %.2f fraction\n", weights[i], profits[i], solution[i]);
    }

    printf("\nMaximum Total Profit: %.2f\n", totalprofit);
}

int main(void) {
    int n;
    float capacity;
    float weights[MAX_ITEMS];
    float profits[MAX_ITEMS];

    printf("FRACTIONAL KNAPSACK PROBLEM (GREEDY APPROACH)\n");

    // 1. Validate number of items
    printf("Enter the number of items (1 to %d): ", MAX_ITEMS);
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX_ITEMS) {
        printf("Error: Invalid number of items! Must be an integer between 1 and %d.\n", MAX_ITEMS);
        return 1;
    }

    // 2. Validate knapsack capacity
    printf("Enter the capacity of knapsack: ");
    if (scanf("%f", &capacity) != 1 || capacity <= 0.0f) {
        printf("Error: Invalid capacity! Must be a positive number.\n");
        return 1;
    }

    // 3. Validate weight and profit entries
    printf("Enter weight and profit for each item:\n");
    for (int i = 0; i < n; i++) {
        printf("Item %d (weight profit): ", i + 1);
        if (scanf("%f %f", &weights[i], &profits[i]) != 2 || weights[i] <= 0.0f || profits[i] < 0.0f) {
            printf("Error: Invalid input for Item %d! Weight must be > 0 and profit must be >= 0.\n", i + 1);
            return 1;
        }
    }

    fractionalKnapsack(n, capacity, weights, profits);

    return 0;
}