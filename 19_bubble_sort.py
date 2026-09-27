n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

ascending = []

for i in range(n):
    ascending.append(arr[i])

i = 0

while i < n - 1:
    j = 0

    while j < n - i - 1:
        if ascending[j] > ascending[j + 1]:
            temp = ascending[j]
            ascending[j] = ascending[j + 1]
            ascending[j + 1] = temp

        j = j + 1

    i = i + 1

descending = []

for i in range(n):
    descending.append(arr[i])

i = 0

while i < n - 1:
    j = 0

    while j < n - i - 1:
        if descending[j] < descending[j + 1]:
            temp = descending[j]
            descending[j] = descending[j + 1]
            descending[j + 1] = temp

        j = j + 1

    i = i + 1

print("Ascending order:")

for i in range(n):
    print(ascending[i], end=" ")

print()

print("Descending order:")

for i in range(n):
    print(descending[i], end=" ")

print()
