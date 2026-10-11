#include <stdio.h>

int main() {
    int a[2][2], b[2][2], c[2][2];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            scanf("%d", &a[i][j]);

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            scanf("%d", &b[i][j]);

    int p = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1]);
    int q = (a[1][0] + a[1][1]) * b[0][0];
    int r = a[0][0] * (b[0][1] - b[1][1]);
    int s = a[1][1] * (b[1][0] - b[0][0]);
    int t = (a[0][0] + a[0][1]) * b[1][1];
    int u = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1]);
    int v = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1]);

    c[0][0] = p + s - t + v;
    c[0][1] = r + t;
    c[1][0] = q + s;
    c[1][1] = p + r - q + u;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
    return 0;
}
