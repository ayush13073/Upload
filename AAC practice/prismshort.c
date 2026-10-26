#include <stdio.h>

#define MAX 100
#define INF 10000000

void prism(int n, int graph[MAX][MAX]) {
    int selected[MAX] = {0};
    long long total = 0;

    selected[0] = 1;

    printf("\nEdges in the Minimum Spanning Tree:\n");
    for (int edge = 0; edge < n - 1; edge++) {
        int u = -1;
        int v = -1;
        int min = INF;

        for (int i = 0; i < n; i++) {
            if (selected[i]) {
                for (int j = 0; j < n; j++) {
                    if (!selected[j] && graph[i][j] > 0 && graph[i][j] < min) {
                        min = graph[i][j];
                        u = i;
                        v = j;
                    }
                }
            }
        }

        // Check if graph is disconnected
        if (u == -1) {
            printf("\nGraph is disconnected. Minimum Spanning Tree cannot be formed.\n");
            return;
        }

        printf("%d - %d : %d\n", u + 1, v + 1, min);
        total += min;
        selected[v] = 1;
    }

    printf("\nTotal Minimum Cost: %lld\n", total);
}

int main(void) {
    int n;
    int graph[MAX][MAX];

    printf("PRIM'S MINIMUM SPANNING TREE ALGORITHM\n");
    printf("Enter number of vertices (1 to %d): ", MAX);
    
    // Validate number of vertices
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX) {
        printf("Error: Invalid number of vertices! Please enter an integer between 1 and %d.\n", MAX);
        return 1;
    }

    printf("Enter adjacency matrix (%d x %d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // Validate integer input and non-negative edge weight
            if (scanf("%d", &graph[i][j]) != 1 || graph[i][j] < 0) {
                printf("Error: Invalid matrix entry at [%d][%d]! Must be a non-negative integer.\n", i + 1, j + 1);
                return 1;
            }
            // Ensure self-loops are set to 0
            if (i == j) {
                graph[i][j] = 0;
            }
        }
    }

    prism(n, graph);

    return 0;
}