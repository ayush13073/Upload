#include <stdio.h>
#define MAX_SIZE 1000
int getMax(int arr[], int n){   
    int max = arr[0];
    for(int i = 1; i < n;i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }

    return max;
}

void countsort(int arr[], int n, int exp){
    int output[MAX_SIZE];
    int count[10] = {0};

    for(int i = 0 ;i < n;i++){
        count[(arr[i] / exp) % 10]++;
    }

    for(int i = 1; i < 10; i++){
        count[i] += count[i - 1];

    }

    for(int i = n - 1; i >= 0; i--){
        int digit = (arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    for(int i =0 ; i < n;i++){
        arr[i] = output[i];
    }
}

void radix_sort(int arr[], int n ){
    if(n <= 1){
        return;
    }

    int max = getMax(arr, n);
    for(int exp = 1; max / exp > 0; exp *= 10){
        countsort(arr, n , exp);
    }
}
int main() {
    int n;

    printf("Enter the size of an array: ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX_SIZE) {
        printf("Invalid array size.\n");
        return 0;
    }

    int arr[MAX_SIZE];

    printf("Enter the elements in the array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    radix_sort(arr, n);

    printf("Sorted elements are: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}