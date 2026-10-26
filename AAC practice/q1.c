#include <stdio.h>

#define MAX_SIZE 1000

/* 
 * VARIATION: Lomuto Partition Scheme
 * - Pivot: Chosen as the last element (arr[high]).
 * - Single-pass scan: A pointer 'j' traverses left to right, maintaining 
 *   a boundary 'i' for elements smaller than or equal to the pivot.
 * - Simpler logic, but does more swaps on average than Hoare's scheme.
 */
int lomutoPartition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

void quickSortLomuto(int arr[], int low, int high) {
    if (low < high) {
        int pIndex = lomutoPartition(arr, low, high);
        quickSortLomuto(arr, low, pIndex - 1);
        quickSortLomuto(arr, pIndex + 1, high);
    }
}

int main() {
    int n;

    printf("Enter the size of an array: ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX_SIZE) {
        printf("Invalid array size\n");
        return 0;
    }

    int arr[MAX_SIZE];

    printf("Enter the elements in the array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    quickSortLomuto(arr, 0, n - 1);

    printf("Sorted elements are: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}