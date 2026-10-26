#include <stdio.h>
#include <stdbool.h>

#define MAX 20
#define INF 99999

int find_min_key(int key[], bool in_mst[], int n) {
    int min = INF;
    int min_index = -1;

    for (int v = 0; v < n; v++) {
        if (!in_mst[v] && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

void prim_mst(int cost[MAX][MAX], int n) {
    int parent[MAX];
    int key[MAX];
    bool in_mst[MAX];

    for (int i = 0; i < n; i++) {
        key[i] = INF;
        in_mst[i] = false;
    }

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < n - 1; count++) {
        int u = find_min_key(key, in_mst, n);

        if (u == -1) break;

        in_mst[u] = true;

        for (int v = 0; v < n; v++) {
            if (cost[u][v] && !in_mst[v] && cost[u][v] < key[v]) {
                parent[v] = u;
                key[v] = cost[u][v];
            }
        }
    }

    int total_cost = 0;
    printf("\nEdge \tWeight\n");
    for (int i = 1; i < n; i++) {
        printf("%d - %d \t%d\n", parent[i], i, cost[i][parent[i]]);
        total_cost += cost[i][parent[i]];
    }
    printf("Total Cost of Minimum Spanning Tree: %d\n", total_cost);
}

int main() {
    int n;
    int cost[MAX][MAX];

    printf("Enter the number of vertices: ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of vertices.\n");
        return 1;
    }

    printf("Enter the adjacency matrix (use %d for infinity / no edge):\n", INF);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
        }
    }

    prim_mst(cost, n);

    return 0;
}