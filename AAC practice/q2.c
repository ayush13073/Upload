#include <stdio.h>

#define MAX_SIZE 1000

/* 
 * VARIATION: Hoare Partition Scheme (Striver's implementation)
 * - Pivot: Chosen as the first element (arr[low]).
 * - Two-pointer scan: 'i' advances from the left looking for elements greater than the pivot,
 *   while 'j' retreats from the right looking for elements smaller than or equal to the pivot.
 * - Swaps elements until pointers cross, resulting in ~3x fewer swaps on average.
 */
int hoarePartition(int arr[], int low, int high) {
    int pivot = arr[low];
    int i = low;
    int j = high;

    while (i < j) {
        while (arr[i] <= pivot && i <= high - 1) {
            i++;
        }
        while (arr[j] > pivot && j >= low + 1) {
            j--;
        }
        if (i < j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[low];
    arr[low] = arr[j];
    arr[j] = temp;

    return j;
}

void quickSortHoare(int arr[], int low, int high) {
    if (low < high) {
        int pIndex = hoarePartition(arr, low, high);
        quickSortHoare(arr, low, pIndex - 1);
        quickSortHoare(arr, pIndex + 1, high);
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

    quickSortHoare(arr, 0, n - 1);

    printf("Sorted elements are: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}