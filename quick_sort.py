def quick_sort(arr):
    # 재귀함수 종료 시키는 부분
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    less_arr = []
    greater_arr = []
    equal_arr = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            less_arr.append(arr[i])
        elif pivot == arr[i]:
            equal_arr.append(arr[i])
        else:
            greater_arr.append(arr[i])
    return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

arr = [1, 2, 3, 4, 6, 5, 7, 1]
print(quick_sort(arr))