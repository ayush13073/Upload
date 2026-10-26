#include<stdio.h>

#define maxx 100
#define inf 99999

void floydwarshall(int n , int dist[maxx][maxx]){
    for(int k = 0; k < n; k++){
        for(int i = 0 ; i < n; i++){
            for(int j = 0; j < n; j++){
                if(dist[i][k] != inf && dist[k][j] != inf){
                    if(dist[i][k] + dist[k][j] < dist[i][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }
    printf("Short distance between every nodes");
    for(int i = 0; i < n;i++){
        for(int j = 0; j < n; j++){
            if(dist[i][j] >= inf){
                printf("%7s", "inf");
            }else{
                printf("%7d", dist[i][j]);
            }
        }
        printf("\n");
    }
}

int main(){
    int n; 
    int dist[maxx][maxx];


    printf("Enter the vertices : ");
    scanf("%d", &n);

    printf("enter adjacency matric");

    for(int i = 0; i  < n;i++){
        for(int j = 0; j < n;j++){
            scanf("%d", &dist[i][j]);
        }
    }
    floydwarshall(n, dist);
}