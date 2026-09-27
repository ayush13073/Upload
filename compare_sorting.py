import random
import time


def selection_sort(arr, n):
    i = 0

    while i < n - 1:
        min_index = i
        j = i + 1

        while j < n:
            if arr[j] < arr[min_index]:
                min_index = j

            j = j + 1

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

        i = i + 1


def bubble_sort(arr, n):
    i = 0

    while i < n - 1:
        j = 0

        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

            j = j + 1

        i = i + 1


def insertion_sort(arr, n):
    i = 1

    while i < n:
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
        i = i + 1


def count_sort(arr, n):
    minimum = arr[0]
    maximum = arr[0]

    i = 1

    while i < n:
        if arr[i] < minimum:
            minimum = arr[i]

        if arr[i] > maximum:
            maximum = arr[i]

        i = i + 1

    range_size = maximum - minimum + 1

    count = []

    i = 0

    while i < range_size:
        count.append(0)
        i = i + 1

    i = 0

    while i < n:
        count[arr[i] - minimum] = count[arr[i] - minimum] + 1
        i = i + 1

    index = 0
    i = 0

    while i < range_size:
        j = 0

        while j < count[i]:
            arr[index] = i + minimum
            index = index + 1
            j = j + 1

        i = i + 1


def counting_sort_radix(arr, n, position):
    output = []

    i = 0

    while i < n:
        output.append(0)
        i = i + 1

    count = []

    i = 0

    while i < 10:
        count.append(0)
        i = i + 1

    i = 0

    while i < n:
        digit = (arr[i] // position) % 10
        count[digit] = count[digit] + 1
        i = i + 1

    i = 1

    while i < 10:
        count[i] = count[i] + count[i - 1]
        i = i + 1

    i = n - 1

    while i >= 0:
        digit = (arr[i] // position) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] = count[digit] - 1
        i = i - 1

    i = 0

    while i < n:
        arr[i] = output[i]
        i = i + 1


def radix_sort(arr, n):
    maximum = arr[0]

    i = 1

    while i < n:
        if arr[i] > maximum:
            maximum = arr[i]

        i = i + 1

    position = 1

    while maximum // position > 0:
        counting_sort_radix(arr, n, position)
        position = position * 10


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


def measure_selection(arr):
    n = len(arr)
    start = time.time()
    selection_sort(arr, n)
    end = time.time()
    return end - start


def measure_bubble(arr):
    n = len(arr)
    start = time.time()
    bubble_sort(arr, n)
    end = time.time()
    return end - start


def measure_insertion(arr):
    n = len(arr)
    start = time.time()
    insertion_sort(arr, n)
    end = time.time()
    return end - start


def measure_count(arr):
    n = len(arr)
    start = time.time()
    count_sort(arr, n)
    end = time.time()
    return end - start


def measure_radix(arr):
    n = len(arr)
    start = time.time()
    radix_sort(arr, n)
    end = time.time()
    return end - start


def measure_heap(arr):
    n = len(arr)
    start = time.time()
    heap_sort(arr, n)
    end = time.time()
    return end - start


def measure_quick(arr):
    n = len(arr)
    start = time.time()
    quick_sort(arr, 0, n - 1)
    end = time.time()
    return end - start


def measure_merge(arr):
    n = len(arr)
    start = time.time()
    merge_sort(arr, 0, n - 1)
    end = time.time()
    return end - start


sizes = [1000, 2000, 5000]

print("SORTING ALGORITHM COMPARISON")
print()

print("Size\tSelection\tBubble\t\tInsertion\tCount\t\tRadix\t\tHeap\t\tQuick\t\tMerge")
print("-" * 115)

for size in sizes:
    original = []

    i = 0

    while i < size:
        original.append(random.randint(0, 10000))
        i = i + 1

    arr1 = []

    i = 0

    while i < size:
        arr1.append(original[i])
        i = i + 1

    arr2 = []

    i = 0

    while i < size:
        arr2.append(original[i])
        i = i + 1

    arr3 = []

    i = 0

    while i < size:
        arr3.append(original[i])
        i = i + 1

    arr4 = []

    i = 0

    while i < size:
        arr4.append(original[i])
        i = i + 1

    arr5 = []

    i = 0

    while i < size:
        arr5.append(original[i])
        i = i + 1

    arr6 = []

    i = 0

    while i < size:
        arr6.append(original[i])
        i = i + 1

    arr7 = []

    i = 0

    while i < size:
        arr7.append(original[i])
        i = i + 1

    arr8 = []

    i = 0

    while i < size:
        arr8.append(original[i])
        i = i + 1

    selection_time = measure_selection(arr1)
    bubble_time = measure_bubble(arr2)
    insertion_time = measure_insertion(arr3)
    count_time = measure_count(arr4)
    radix_time = measure_radix(arr5)
    heap_time = measure_heap(arr6)
    quick_time = measure_quick(arr7)
    merge_time = measure_merge(arr8)

    print(str(size) + "\t" +
          str(round(selection_time, 6)) + "\t\t" +
          str(round(bubble_time, 6)) + "\t\t" +
          str(round(insertion_time, 6)) + "\t\t" +
          str(round(count_time, 6)) + "\t\t" +
          str(round(radix_time, 6)) + "\t\t" +
          str(round(heap_time, 6)) + "\t\t" +
          str(round(quick_time, 6)) + "\t\t" +
          str(round(merge_time, 6)))
