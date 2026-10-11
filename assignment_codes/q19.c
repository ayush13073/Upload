#include <stdio.h>

void bubble_sort(int arr[], int n, int asc) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (asc ? (arr[j] > arr[j + 1]) : (arr[j] < arr[j + 1])) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
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
    bubble_sort(arr1, n, 1);
    for (int i = 0; i < n; i++) printf("%d ", arr1[i]);
    printf("\n");
    bubble_sort(arr2, n, 0);
    for (int i = 0; i < n; i++) printf("%d ", arr2[i]);
    printf("\n");
    return 0;
}
