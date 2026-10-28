"""
Question 4: Print Floyd's Triangle.
1
2 3
4 5 6
7 8 9 10
"""


def main():
    rows = int(input("Enter the number of rows: "))
    if rows <= 0:
        print("Please enter a positive number of rows.")
        return

    number = 1
    for i in range(1, rows + 1):
        row = []
        for _ in range(i):
            row.append(str(number))
            number += 1
        print(" ".join(row))


if __name__ == "__main__":
    main()
