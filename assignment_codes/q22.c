#include <stdio.h>

int getMax(int arr[], int n) {
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx) mx = arr[i];
    return mx;
}

void countSortDigit(int arr[], int n, int exp, int asc) {
    int output[n];
    int count[10] = {0};
    for (int i = 0; i < n; i++) count[(arr[i] / exp) % 10]++;

    if (asc) {
        for (int i = 1; i < 10; i++) count[i] += count[i - 1];
        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
    } else {
        for (int i = 8; i >= 0; i--) count[i] += count[i + 1];
        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
    }

    for (int i = 0; i < n; i++) arr[i] = output[i];
}

void radix_sort(int arr[], int n, int asc) {
    int m = getMax(arr, n);
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSortDigit(arr, n, exp, asc);
}

int main() {
    int n;
    scanf("%d", &n);
    int arr1[n], arr2[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr1[i]);
        arr2[i] = arr1[i];
    }
    radix_sort(arr1, n, 1);
    for (int i = 0; i < n; i++) printf("%d ", arr1[i]);
    printf("\n");
    radix_sort(arr2, n, 0);
    for (int i = 0; i < n; i++) printf("%d ", arr2[i]);
    printf("\n");
    return 0;
}
