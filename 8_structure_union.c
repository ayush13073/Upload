#include <stdio.h>

struct Student
{
    int roll;
    char name[50];
    float marks;
};

union Data
{
    int roll;
    char name[50];
    float marks;
};

int main()
{
    struct Student student;
    union Data data;

    printf("Enter student roll number: ");
    scanf("%d", &student.roll);

    printf("Enter student name: ");
    scanf("%s", student.name);

    printf("Enter student marks: ");
    scanf("%f", &student.marks);

    printf("\nStructure:\n");
    printf("Roll Number: %d\n", student.roll);
    printf("Name: %s\n", student.name);
    printf("Marks: %.2f\n", student.marks);

    printf("\nUnion:\n");

    data.roll = student.roll;
    printf("Roll Number: %d\n", data.roll);

    data.marks = student.marks;
    printf("Marks: %.2f\n", data.marks);

    return 0;
}
