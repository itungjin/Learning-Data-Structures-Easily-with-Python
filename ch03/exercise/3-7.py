# 알고리즘 수행 시간
# 점근적 수행 시간

def sample(array, n):
    if n == 1:
        return 1
    sum = 0
    for i in range(1, n+1):
        sum += array[i]
    temp = sum + sample(array, n-1)
    return temp

# n²
