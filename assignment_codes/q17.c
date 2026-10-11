#include <stdio.h>

long long sum_iter(int n) {
    long long s = 0;
    for (int i = 1; i <= n; i++) s += i;
    return s;
}

long long sum_rec(int n) {
    if (n <= 0) return 0;
    return n + sum_rec(n - 1);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\n", sum_iter(n));
    printf("%lld\n", sum_rec(n));
    return 0;
}
