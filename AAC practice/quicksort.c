#include<stdio.h>


int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for(int j  = low; j < high; j++){
        if(arr[j] <= pivot){
            i++;
            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high ] = temp;
    return  i + 1;

}

void quick_sort(int arr[], int low, int high){
    if(low < high) {
        int pIndex = partition(arr, low, high);
        quick_sort(arr,low,pIndex -1 );
        quick_sort(arr,pIndex + 1, high);
    }
}
int main() {
    int n ;
    printf("Enter the size of an array : ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter the elements in the array : ");
    for(int i = 0; i < n; i++){
        scanf("%d",&arr[i]);
    }

    quick_sort(arr,0,n -1 );

    printf("Sorted elements are : ");
    for(int i = 0; i < n;i++){
        printf("%d ", arr[i]);

    }
    return 0;
}