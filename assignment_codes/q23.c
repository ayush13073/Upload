#include <stdio.h>

int bin_search_iter(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) return mid;
        if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int bin_search_rec(int arr[], int low, int high, int key) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == key) return mid;
    if (arr[mid] < key) return bin_search_rec(arr, mid + 1, high, key);
    return bin_search_rec(arr, low, mid - 1, key);
}

int main() {
    int n, key;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    scanf("%d", &key);
    printf("%d\n", bin_search_iter(arr, n, key));
    printf("%d\n", bin_search_rec(arr, 0, n - 1, key));
    return 0;
}
