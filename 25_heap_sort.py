def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp

        heapify(arr, n, largest)


def heap_sort(arr, n):
    i = n // 2 - 1

    while i >= 0:
        heapify(arr, n, i)
        i = i - 1

    i = n - 1

    while i > 0:
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

        heapify(arr, i, 0)

        i = i - 1


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

heap_sort(arr, n)

print("Sorted array:")

for i in range(n):
    print(arr[i], end=" ")

print()
