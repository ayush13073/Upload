rows1 = int(input("Enter number of rows of first matrix: "))
columns1 = int(input("Enter number of columns of first matrix: "))

rows2 = int(input("Enter number of rows of second matrix: "))
columns2 = int(input("Enter number of columns of second matrix: "))

if columns1 != rows2:
    print("Matrix multiplication is not possible.")
else:
    matrix1 = []
    matrix2 = []

    print("Enter elements of first matrix:")

    for i in range(rows1):
        row = []

        for j in range(columns1):
            value = int(input("Enter element: "))
            row.append(value)

        matrix1.append(row)

    print("Enter elements of second matrix:")

    for i in range(rows2):
        row = []

        for j in range(columns2):
            value = int(input("Enter element: "))
            row.append(value)

        matrix2.append(row)

    result = []

    for i in range(rows1):
        row = []

        for j in range(columns2):
            sum = 0

            for k in range(columns1):
                sum = sum + matrix1[i][k] * matrix2[k][j]

            row.append(sum)

        result.append(row)

    print("Matrix multiplication:")

    for i in range(rows1):
        for j in range(columns2):
            print(result[i][j], end=" ")

        print()
