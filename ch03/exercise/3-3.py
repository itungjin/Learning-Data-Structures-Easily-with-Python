# 알고리즘 복잡도
# 점근적 복잡도

def sample(array, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += array[i] * array[j]
    return sum

# O(n²)
# Ω(n²)
# Θ(n²)
