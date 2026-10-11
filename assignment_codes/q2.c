#include <stdio.h>

long long fib_iter(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

long long fib_rec(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fib_rec(n - 1) + fib_rec(n - 2);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\n", fib_iter(n));
    printf("%lld\n", fib_rec(n));
    return 0;
}
