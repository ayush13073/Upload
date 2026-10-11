#include <stdio.h>
#include <string.h>

int main() {
    char s[1000];
    scanf("%s", s);
    int len = strlen(s);
    int flag = 1;
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - 1 - i]) {
            flag = 0;
            break;
        }
    }
    if (flag) printf("Palindrome\n");
    else printf("Not Palindrome\n");
    return 0;
}
