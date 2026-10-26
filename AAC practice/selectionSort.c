#include<stdio.h>

void selection_sort(int arr[], int n){
    for (int i = 0; i < n- 1; i++){
        int mini = i;
        for(int j = i; j < n; j++){
            if(arr[j] < arr[mini]){
                mini = j;
            }


        }

        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i] = temp;
    
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

    selection_sort(arr,n);

    printf("Sorted elements are : ");
    for(int i = 0; i < n;i++){
        printf("%d ", arr[i]);

    }
    return 0;
}