n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

minimum = arr[0]

i = 1

while i < n:
    if arr[i] < minimum:
        minimum = arr[i]

    i = i + 1

print("Minimum number:", minimum)
