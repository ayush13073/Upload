#include <stdio.h>

struct Item {
    int value;
    int weight;
};

void sortItems(struct Item arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            double r1 = (double)arr[j].value / arr[j].weight;
            double r2 = (double)arr[j + 1].value / arr[j + 1].weight;
            if (r1 < r2) {
                struct Item temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n, W;
    scanf("%d %d", &n, &W);
    struct Item arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &arr[i].value, &arr[i].weight);
    }
    sortItems(arr, n);

    double totalValue = 0.0;
    int currentWeight = 0;

    for (int i = 0; i < n; i++) {
        if (currentWeight + arr[i].weight <= W) {
            currentWeight += arr[i].weight;
            totalValue += arr[i].value;
        } else {
            int remain = W - currentWeight;
            totalValue += arr[i].value * ((double)remain / arr[i].weight);
            break;
        }
    }
    printf("%.2f\n", totalValue);
    return 0;
}
