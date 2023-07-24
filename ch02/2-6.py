# 선택 정렬(재귀 버전)

def selection_sort(arr, n):
    if (n > 1):
        k = arr.index(max(arr[0:n]))
        arr[k], arr[n-1] = arr[n-1], arr[k]
        selection_sort(arr, n-1)
