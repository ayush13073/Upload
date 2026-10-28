"""
Question 2: Generate a multiplication matrix (10 x 10).
"""


def main():
    size = 10
    print("Multiplication Matrix (10 x 10):\n")
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(f"{i * j:5d}")
        print("".join(row))


if __name__ == "__main__":
    main()
