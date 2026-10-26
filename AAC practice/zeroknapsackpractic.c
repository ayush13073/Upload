#include<stdio.h>

#define MAXitem 100
#define maxcap 1000

int max(int a, int b){
    return (a > b) ? a : b;
}

void knapsack01(int n , int W, int weights[], int values[]){
    int dp[MAXitem + 1][maxcap + 1];

    for(int i = 0; i <= n; i++){
        for(int w = 0; w<=n ; w++){
            if(i == 0 || w == 0){
                dp[i][w] = 0;
            }else if(weights[i - 1] <= w){
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i -1][w]  );
            }else{
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    printf("Maximum value achievable : %d\n", dp[n][W]);

    printf("Items selected ( 1 - indexed)\n");

    int w = W;
    for(int i = n; i > 0 && dp[i][w] > 0;i--){
        if(dp[i][w] != dp[i - 1][w]){
            printf("item %d (weight : %d , value : %d)\n", i, weights[i- 1], values[i - 1]);
            w -= weights[i - 1];
        }
    }

}
int main(void) {
    int n, W;
    int weights[MAXitem], values[MAXitem];

    /*
     * INPUT INSTRUCTIONS:
     * 1. Enter number of items (n).
     * 2. Enter maximum knapsack capacity (W).
     * 3. Enter weights of the n items separated by spaces.
     * 4. Enter corresponding values/profits of the n items separated by spaces.
     */

    printf("0/1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING)\n");
    printf("Enter number of items: ");
    scanf("%d", &n);

    printf("Enter maximum knapsack capacity: ");
    scanf("%d", &W);

    printf("Enter weights of %d items: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &weights[i]);
    }

    printf("Enter values of %d items: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &values[i]);
    }

    knapsack01(n, W, weights, values);

    return 0;
}