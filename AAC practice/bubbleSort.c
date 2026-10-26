#include<stdio.h>

void bubble_sort(int arr[], int n){
    
    for(int i = n -1 ;i >= 1; i--){
        for(int j = 0; j < i ; j++){
            if(arr[j] > arr[j + 1]){
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

            }
        }
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

    bubble_sort(arr,n);

    printf("Sorted elements are : ");
    for(int i = 0; i < n;i++){
        printf("%d ", arr[i]);

    }
    return 0;
}