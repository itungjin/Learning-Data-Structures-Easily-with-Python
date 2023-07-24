# 알고리즘 수행 시간

def sample(array, n):
    sum = 0
    for i in range(n):
        sum += array[i]
    return sum

# 수행 시간은 n의 1차에 비례
