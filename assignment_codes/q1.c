#include <stdio.h>

long long fact_iter(int n) {
    long long res = 1;
    for (int i = 2; i <= n; i++) res *= i;
    return res;
}

long long fact_rec(int n) {
    if (n <= 1) return 1;
    return n * fact_rec(n - 1);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\n", fact_iter(n));
    printf("%lld\n", fact_rec(n));
    return 0;
}
