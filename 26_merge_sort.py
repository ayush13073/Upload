def merge(arr, low, mid, high):
    left = []
    right = []

    i = low

    while i <= mid:
        left.append(arr[i])
        i = i + 1

    i = mid + 1

    while i <= high:
        right.append(arr[i])
        i = i + 1

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        merge(arr, low, mid, high)


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

merge_sort(arr, 0, n - 1)

print("Sorted array:")

for i in range(n):
    print(arr[i], end=" ")

print()
