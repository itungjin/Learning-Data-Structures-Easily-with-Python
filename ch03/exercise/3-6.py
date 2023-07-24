# 알고리즘 복잡도
# 점근적 복잡도

import random


def sample(array, n):
    if n == 1:
        return 1
    elif random.randint <= 50:
        sum = 0
        for i in range(1, n+1):
            sum += array[i]
    sample(array, n-1)

# O(n²)
# Ω(n)
