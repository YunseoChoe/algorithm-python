def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr

arr = [6, 4, 3, 2, 5, 1]
print(insertion_sort(arr))

