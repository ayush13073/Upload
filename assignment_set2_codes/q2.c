#include <stdio.h>

void dfs(int v, int n, int adj[n][n], int visited[], int stack[], int *top) {
    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i]) {
            dfs(i, n, adj, visited, stack, top);
        }
    }
    stack[++(*top)] = v;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int adj[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            adj[i][j] = 0;
        }
    }
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u][v] = 1;
    }

    int visited[n], stack[n], top = -1;
    for (int i = 0; i < n; i++) visited[i] = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, n, adj, visited, stack, &top);
        }
    }

    while (top >= 0) {
        printf("%d ", stack[top--]);
    }
    printf("\n");
    return 0;
}
