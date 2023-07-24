# 선택 정렬
# 양의 정수 n에 대해 selection_sort(arr, n)을 호출할 때 selection_sort()의 총 호출 횟수


def selection_sort(arr, n):
    if n > 1:
        k = arr.index(max(arr[0:n]))
        arr[k], arr[n-1] = arr[n-1], arr[k]
        selection_sort(arr, n-1)


# selection_sort(arr, 1)을 호출할 때 selection_sort()는 1번 호출
# selection_sort(arr, 2)을 호출할 때 selection_sort()는 2번 호출
# selection_sort(arr, 3)을 호출할 때 selection_sort()는 3번 호출
# selection_sort(arr, 4)을 호출할 때 selection_sort()는 4번 호출
# selection_sort(arr, 5)을 호출할 때 selection_sort()는 5번 호출
