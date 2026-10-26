#include<stdio.h>

void count_sort(int arr[], int n){
    
    if (n <= 1) {
        return;
    }
    int max = arr[0];
    for(int i = 1; i < n ;i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }

    int count[max + 1];
    for(int i = 0; i <= max; i++){
        count[i] = 0;
    }

    for(int i = 0;i < n;i++){
        count[arr[i]]++;
    }

    int k = 0;
    for(int i = 0; i <= max; i++){
        while(count[i] > 0){
            arr[k] = i;
            k++;
            count[i]--;
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

    count_sort(arr,n);

    printf("Sorted elements are : ");
    for(int i = 0; i < n;i++){
        printf("%d ", arr[i]);

    }
    return 0;
}