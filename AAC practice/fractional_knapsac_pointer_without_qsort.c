#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    double weight;
    double value;
    double ratio;
} Item;

// Pointer-based swap function
void swapItems(Item *a, Item *b) {
    Item temp = *a;
    *a = *b;
    *b = temp;
}

// Pointer-based Bubble Sort (descending order by ratio)
void sortItems(Item *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            // Using pointer arithmetic and arrow operator
            Item *curr = arr + j;
            Item *next = arr + (j + 1);

            if (curr->ratio < next->ratio) {
                swapItems(curr, next);
            }
        }
    }
}

int main(void) {
    int n;
    double capacity, totalValue = 0.0, remaining;

    printf("FRACTIONAL KNAPSACK - GREEDY METHOD\nEnter number of items (1-10000): ");
    if (scanf("%d", &n) != 1 || n < 1 || n > 10000) {
        printf("Invalid number of items.\n");
        return 1;
    }

    printf("Enter knapsack capacity: ");
    if (scanf("%lf", &capacity) != 1 || capacity < 0) {
        printf("Invalid capacity.\n");
        return 1;
    }

    // Dynamic memory allocation using pointers
    Item *items = (Item *)malloc((size_t)n * sizeof(Item));
    if (!items) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        Item *ptr = items + i; // Pointer traversal
        printf("Enter weight and value for item %d: ", i + 1);
        if (scanf("%lf %lf", &(ptr->weight), &(ptr->value)) != 2 || ptr->weight <= 0 || ptr->value < 0) {
            printf("Invalid weight or value. Weight must be positive and value non-negative.\n");
            free(items);
            return 1;
        }
        ptr->id = i + 1;
        ptr->ratio = ptr->value / ptr->weight;
    }

    // Manual sort without qsort
    sortItems(items, n);

    remaining = capacity;
    printf("\nSelected fractions:\n");
    for (int i = 0; i < n && remaining > 0; i++) {
        Item *curr = items + i;
        double fraction = (curr->weight <= remaining) ? 1.0 : (remaining / curr->weight);

        if (fraction > 0) {
            printf("Item %d: %.2f%% taken\n", curr->id, fraction * 100.0);
            totalValue += curr->value * fraction;
            remaining -= curr->weight * fraction;
        }
    }

    printf("Maximum obtainable value: %.2f\n", totalValue);

    free(items);
    items = NULL;
    return 0;
}