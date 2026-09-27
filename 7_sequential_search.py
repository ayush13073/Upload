def sequential_search_iterative(arr, n, key):
    i = 0

    while i < n:
        if arr[i] == key:
            return i
        i = i + 1

    return -1


def sequential_search_recursive(arr, n, key, i):
    if i == n:
        return -1

    if arr[i] == key:
        return i

    return sequential_search_recursive(arr, n, key, i + 1)


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

key = int(input("Enter the element to search: "))

result1 = sequential_search_iterative(arr, n, key)
result2 = sequential_search_recursive(arr, n, key, 0)

if result1 == -1:
    print("Element not found using iterative search.")
else:
    print("Element found at position", result1 + 1, "using iterative search.")

if result2 == -1:
    print("Element not found using recursive search.")
else:
    print("Element found at position", result2 + 1, "using recursive search.")
