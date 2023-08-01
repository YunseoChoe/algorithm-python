def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    # Split.
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    # Merge and sort.
    merged_arr = []
    l = r = 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            merged_arr.append(L[l])
            l += 1
        else:
            merged_arr.append(R[r])
            r += 1

    if l < len(L):
        merged_arr += L[l:]
    if r < len(R):
        merged_arr += R[r:]

    return merged_arr

arr = [6, 4, 2, 5, 3, 1]
print(merge_sort(arr))

