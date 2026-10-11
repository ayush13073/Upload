#include <stdio.h>

void sel_sort(int arr[], int n, int asc) {
    for (int i = 0; i < n - 1; i++) {
        int target = i;
        for (int j = i + 1; j < n; j++) {
            if (asc ? (arr[j] < arr[target]) : (arr[j] > arr[target])) {
                target = j;
            }
        }
        int temp = arr[target];
        arr[target] = arr[i];
        arr[i] = temp;
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
    sel_sort(arr1, n, 1);
    for (int i = 0; i < n; i++) printf("%d ", arr1[i]);
    printf("\n");
    sel_sort(arr2, n, 0);
    for (int i = 0; i < n; i++) printf("%d ", arr2[i]);
    printf("\n");
    return 0;
}
