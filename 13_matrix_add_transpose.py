rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []

print("Enter elements of first matrix:")

for i in range(rows):
    row = []

    for j in range(columns):
        value = int(input("Enter element: "))
        row.append(value)

    matrix1.append(row)

print("Enter elements of second matrix:")

for i in range(rows):
    row = []

    for j in range(columns):
        value = int(input("Enter element: "))
        row.append(value)

    matrix2.append(row)

addition = []

for i in range(rows):
    row = []

    for j in range(columns):
        row.append(matrix1[i][j] + matrix2[i][j])

    addition.append(row)

print("Matrix addition:")

for i in range(rows):
    for j in range(columns):
        print(addition[i][j], end=" ")

    print()

transpose1 = []

for j in range(columns):
    row = []

    for i in range(rows):
        row.append(matrix1[i][j])

    transpose1.append(row)

print("Transpose of first matrix:")

for i in range(columns):
    for j in range(rows):
        print(transpose1[i][j], end=" ")

    print()
