n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

ascending = []

for i in range(n):
    ascending.append(arr[i])

i = 1

while i < n:
    key = ascending[i]
    j = i - 1

    while j >= 0 and ascending[j] > key:
        ascending[j + 1] = ascending[j]
        j = j - 1

    ascending[j + 1] = key
    i = i + 1

descending = []

for i in range(n):
    descending.append(arr[i])

i = 1

while i < n:
    key = descending[i]
    j = i - 1

    while j >= 0 and descending[j] < key:
        descending[j + 1] = descending[j]
        j = j - 1

    descending[j + 1] = key
    i = i + 1

print("Ascending order:")

for i in range(n):
    print(ascending[i], end=" ")

print()

print("Descending order:")

for i in range(n):
    print(descending[i], end=" ")

print()
