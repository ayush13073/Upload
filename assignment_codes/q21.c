#include <stdio.h>

void count_sort(int arr[], int n, int asc) {
    int max = arr[0], min = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }
    int range = max - min + 1;
    int count[range];
    for (int i = 0; i < range; i++) count[i] = 0;
    for (int i = 0; i < n; i++) count[arr[i] - min]++;

    int idx = 0;
    if (asc) {
        for (int i = 0; i < range; i++) {
            while (count[i] > 0) {
                arr[idx++] = i + min;
                count[i]--;
            }
        }
    } else {
        for (int i = range - 1; i >= 0; i--) {
            while (count[i] > 0) {
                arr[idx++] = i + min;
                count[i]--;
            }
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int arr1[n], arr2[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr1[i]);
        arr2[i] = arr1[i];
    }
    count_sort(arr1, n, 1);
    for (int i = 0; i < n; i++) printf("%d ", arr1[i]);
    printf("\n");
    count_sort(arr2, n, 0);
    for (int i = 0; i < n; i++) printf("%d ", arr2[i]);
    printf("\n");
    return 0;
}
