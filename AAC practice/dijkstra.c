#include <stdio.h>
#include <stdbool.h>

#define MAX 100
#define INF 99999

int findMinDistance(int dist[], bool visited[], int n) {
    int min = INF, min_index = -1;

    for (int v = 0; v < n; v++) {
        if (!visited[v] && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

void dijkstra(int n, int graph[MAX][MAX], int src) {
    int dist[MAX];
    bool visited[MAX];

    for (int i = 0; i < n; i++) {
        dist[i] = INF;
        visited[i] = false;
    }

    dist[src] = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = findMinDistance(dist, visited, n);

        if (u == -1) break;

        visited[u] = true;

        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] && dist[u] != INF 
                && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    printf("\nVertex \t Distance from Source %d\n", src + 1);
    for (int i = 0; i < n; i++) {
        if (dist[i] == INF) {
            printf("%d \t INF\n", i + 1);
        } else {
            printf("%d \t %d\n", i + 1, dist[i]);
        }
    }
}

int main(void) {
    int n, src;
    int graph[MAX][MAX];

    /*
     * INPUT INSTRUCTIONS:
     * 1. Enter number of vertices (n).
     * 2. Enter n x n weighted adjacency matrix:
     *    - Put 0 for self-loops (diagonal) and where no direct edge exists.
     *    - Put the weight if a directed or undirected edge exists.
     * 3. Enter source vertex (1-indexed).
     */

    printf("DIJKSTRA'S SHORTEST PATH ALGORITHM\n");
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix (%d x %d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    printf("Enter source vertex (1 to %d): ", n);
    scanf("%d", &src);

    dijkstra(n, graph, src - 1);

    return 0;
}