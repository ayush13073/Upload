def binary_search_iterative(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    if arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, high, key)

    return binary_search_recursive(arr, low, mid - 1, key)


n = int(input("Enter the number of elements: "))

arr = []

print("Enter elements in ascending order:")

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

key = int(input("Enter the element to search: "))

result1 = binary_search_iterative(arr, n, key)
result2 = binary_search_recursive(arr, 0, n - 1, key)

if result1 == -1:
    print("Element not found using iterative search.")
else:
    print("Element found at position", result1 + 1, "using iterative search.")

if result2 == -1:
    print("Element not found using recursive search.")
else:
    print("Element found at position", result2 + 1, "using recursive search.")
