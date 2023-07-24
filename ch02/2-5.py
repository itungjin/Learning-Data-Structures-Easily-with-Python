# 선택 정렬

def selection_sort(arr, n):
    for last in range(n-1, 0, -1):
        k = arr.index(max(arr[0:last+1]))
        arr[k], arr[last] = arr[last], arr[k]
    print(arr)
