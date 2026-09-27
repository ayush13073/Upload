def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low

    while j < high:
        if arr[j] <= pivot:
            i = i + 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        j = j + 1

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        position = partition(arr, low, high)

        quick_sort(arr, low, position - 1)
        quick_sort(arr, position + 1, high)


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

quick_sort(arr, 0, n - 1)

print("Sorted array:")

for i in range(n):
    print(arr[i], end=" ")

print()
