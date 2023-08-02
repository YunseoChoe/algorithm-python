def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

arr = [6, 4, 5, 2, 3, 1]
print(insertion_sort(arr))


# arr = [5, 4, 3, 2, 1]

# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):
#         if arr[j - 1] > arr[j]:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]

# print(arr)