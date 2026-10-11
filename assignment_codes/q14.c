#include <stdio.h>

double fast_power(double x, long long n) {
    if (n == 0) return 1.0;
    if (n < 0) return 1.0 / fast_power(x, -n);
    double half = fast_power(x, n / 2);
    if (n % 2 == 0) return half * half;
    return x * half * half;
}

int main() {
    double x;
    long long n;
    scanf("%lf %lld", &x, &n);
    printf("%.6lf\n", fast_power(x, n));
    return 0;
}
