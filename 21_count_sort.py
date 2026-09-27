n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

minimum = arr[0]
maximum = arr[0]

for i in range(1, n):
    if arr[i] < minimum:
        minimum = arr[i]

    if arr[i] > maximum:
        maximum = arr[i]

range_size = maximum - minimum + 1

count = []

for i in range(range_size):
    count.append(0)

for i in range(n):
    count[arr[i] - minimum] = count[arr[i] - minimum] + 1

ascending = []

for i in range(range_size):
    j = 0

    while j < count[i]:
        ascending.append(i + minimum)
        j = j + 1

descending = []

i = range_size - 1

while i >= 0:
    j = 0

    while j < count[i]:
        descending.append(i + minimum)
        j = j + 1

    i = i - 1

print("Ascending order:")

for i in range(n):
    print(ascending[i], end=" ")

print()

print("Descending order:")

for i in range(n):
    print(descending[i], end=" ")

print()
