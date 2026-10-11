#include <stdio.h>
#include <math.h>

int main() {
    int n, temp, sum = 0, digits = 0;
    scanf("%d", &n);
    temp = n;
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while (temp > 0) {
        int r = temp % 10;
        sum += (int)pow(r, digits);
        temp /= 10;
    }
    if (sum == n) printf("Armstrong\n");
    else printf("Not Armstrong\n");
    return 0;
}
