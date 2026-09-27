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
    min_index = i
    j = i + 1

    while j < n:
        if ascending[j] < ascending[min_index]:
            min_index = j

        j = j + 1

    temp = ascending[i]
    ascending[i] = ascending[min_index]
    ascending[min_index] = temp

    i = i + 1

descending = []

for i in range(n):
    descending.append(arr[i])

i = 0

while i < n - 1:
    max_index = i
    j = i + 1

    while j < n:
        if descending[j] > descending[max_index]:
            max_index = j

        j = j + 1

    temp = descending[i]
    descending[i] = descending[max_index]
    descending[max_index] = temp

    i = i + 1

print("Ascending order:")

for i in range(n):
    print(ascending[i], end=" ")

print()

print("Descending order:")

for i in range(n):
    print(descending[i], end=" ")

print()
