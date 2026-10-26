#include <stdio.h>

#define MAX 100
#define INF 99999

void floydWarshall(int n, int dist[MAX][MAX]) {
    // k is the intermediate vertex
    for (int k = 0; k < n; k++) {
        // i is the source vertex
        for (int i = 0; i < n; i++) {
            // j is the destination vertex
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }

    // Display the shortest distance matrix
    printf("\nShortest distances between every pair of vertices:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] == INF) {
                printf("%7s", "INF");
            } else {
                printf("%7d", dist[i][j]);
            }
        }
        printf("\n");
    }
}

int main(void) {
    int n;
    int dist[MAX][MAX];

    /*
     * INPUT INSTRUCTIONS:
     * 1. Enter number of vertices (n).
     * 2. Enter n x n cost adjacency matrix:
     *    - Put 0 on the diagonal (dist[i][i] = 0).
     *    - Put 99999 (INF) if there is no direct edge between vertex i and j.
     *    - Enter the edge weight if a directed/undirected edge exists.
     */

    printf("FLOYD-WARSHALL ALGORITHM (ALL-PAIRS SHORTEST PATHS)\n");
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter cost adjacency matrix (use %d for INF/no edge):\n", INF);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &dist[i][j]);
        }
    }

    floydWarshall(n, dist);

    return 0;
}