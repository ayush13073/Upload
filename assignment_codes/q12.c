#include <stdio.h>

double power_iter(double x, int n) {
    double res = 1.0;
    int p = n < 0 ? -n : n;
    for (int i = 0; i < p; i++) res *= x;
    return n < 0 ? 1.0 / res : res;
}

double power_rec(double x, int n) {
    if (n == 0) return 1.0;
    if (n < 0) return 1.0 / power_rec(x, -n);
    return x * power_rec(x, n - 1);
}

int main() {
    double x;
    int n;
    scanf("%lf %d", &x, &n);
    printf("%.4lf\n", power_iter(x, n));
    printf("%.4lf\n", power_rec(x, n));
    return 0;
}
