#include <stdio.h>

int seq_search_iter(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) return i;
    }
    return -1;
}

int seq_search_rec(int arr[], int n, int key, int index) {
    if (index >= n) return -1;
    if (arr[index] == key) return index;
    return seq_search_rec(arr, n, key, index + 1);
}

int main() {
    int n, key;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    scanf("%d", &key);
    printf("%d\n", seq_search_iter(arr, n, key));
    printf("%d\n", seq_search_rec(arr, n, key, 0));
    return 0;
}
