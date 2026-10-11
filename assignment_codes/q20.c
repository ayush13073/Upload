#include <stdio.h>

void insertion_sort(int arr[], int n, int asc) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && (asc ? (arr[j] > key) : (arr[j] < key))) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
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
    insertion_sort(arr1, n, 1);
    for (int i = 0; i < n; i++) printf("%d ", arr1[i]);
    printf("\n");
    insertion_sort(arr2, n, 0);
    for (int i = 0; i < n; i++) printf("%d ", arr2[i]);
    printf("\n");
    return 0;
}
