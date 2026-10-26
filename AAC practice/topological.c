#include <stdio.h>

#define MAX 100

// Function to perform Topological Sort using Kahn's Algorithm (in-degree method)
void topologicalSort(int n, int adj[MAX][MAX]) {
    int in_degree[MAX] = {0};
    int queue[MAX];
    int front = 0, rear = -1;
    int topo_order[MAX];
    int count = 0;

    // Step 1: Calculate in-degree of every vertex
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (adj[i][j] == 1) {
                in_degree[j]++;
            }
        }
    }

    // Step 2: Enqueue all vertices with in-degree 0
    for (int i = 0; i < n; i++) {
        if (in_degree[i] == 0) {
            queue[++rear] = i;
        }
    }

    // Step 3: Process the vertices
    while (front <= rear) {
        int u = queue[front++];
        topo_order[count++] = u;

        // Reduce in-degree of all adjacent vertices
        for (int v = 0; v < n; v++) {
            if (adj[u][v] == 1) {
                in_degree[v]--;
                // If in-degree becomes 0, add to queue
                if (in_degree[v] == 0) {
                    queue[++rear] = v;
                }
            }
        }
    }

    // Step 4: Check if topological sorting is possible (DAG check)
    if (count != n) {
        printf("\nThe graph contains a cycle! Topological sort is not possible.\n");
    } else {
        printf("\nTopological Ordering of vertices:\n");
        for (int i = 0; i < count; i++) {
            printf("%d ", topo_order[i] + 1); // 1-based indexing
        }
        printf("\n");
    }
}

int main(void) {
    int n;
    int adj[MAX][MAX];

    /*
     * INPUT INSTRUCTIONS:
     * 1. Enter number of vertices (n).
     * 2. Enter n x n directed adjacency matrix:
     *    - Enter 1 if there is a directed edge from vertex i to vertex j.
     *    - Enter 0 otherwise.
     */

    printf("TOPOLOGICAL SORT (KAHN'S ALGORITHM)\n");
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix (%d x %d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &adj[i][j]);
        }
    }

    topologicalSort(n, adj);

    return 0;
}