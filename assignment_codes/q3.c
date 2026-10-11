#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int nth_prime_iter(int n) {
    int count = 0, num = 1;
    while (count < n) {
        num++;
        if (is_prime(num)) count++;
    }
    return num;
}

int nth_prime_rec_helper(int n, int count, int num) {
    if (is_prime(num)) {
        count++;
        if (count == n) return num;
    }
    return nth_prime_rec_helper(n, count, num + 1);
}

int nth_prime_rec(int n) {
    return nth_prime_rec_helper(n, 0, 2);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", nth_prime_iter(n));
    printf("%d\n", nth_prime_rec(n));
    return 0;
}
