#include <stdio.h>
#include <string.h>

struct Student {
    int id;
    char name[20];
    float marks;
};

union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    struct Student s1;
    s1.id = 101;
    strcpy(s1.name, "Alice");
    s1.marks = 92.5;
    printf("%d %s %.2f\n", s1.id, s1.name, s1.marks);

    union Data d;
    d.i = 10;
    printf("%d\n", d.i);
    d.f = 220.5;
    printf("%.2f\n", d.f);
    strcpy(d.str, "C Lab");
    printf("%s\n", d.str);
    return 0;
}
