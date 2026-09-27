def counting_sort(arr, n, position):
    output = []

    for i in range(n):
        output.append(0)

    count = []

    for i in range(10):
        count.append(0)

    for i in range(n):
        digit = (arr[i] // position) % 10
        count[digit] = count[digit] + 1

    i = 1

    while i < 10:
        count[i] = count[i] + count[i - 1]
        i = i + 1

    i = n - 1

    while i >= 0:
        digit = (arr[i] // position) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] = count[digit] - 1
        i = i - 1

    i = 0

    while i < n:
        arr[i] = output[i]
        i = i + 1


def radix_sort(arr, n):
    maximum = arr[0]

    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]

    position = 1

    while maximum // position > 0:
        counting_sort(arr, n, position)
        position = position * 10


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter a non-negative element: "))
    arr.append(value)

radix_sort(arr, n)

print("Ascending order:")

for i in range(n):
    print(arr[i], end=" ")

print()

print("Descending order:")

i = n - 1

while i >= 0:
    print(arr[i], end=" ")
    i = i - 1

print()
