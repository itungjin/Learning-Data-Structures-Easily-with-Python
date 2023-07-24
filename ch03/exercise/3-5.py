# 알고리즘 복잡도
# 점근적 복잡도

import random


def sample(array, n):
    for i in range(1, n+1):
        if random.randint(1, 100) <= 50:
            sum = 0
            for i in range(1, n+1):
                sum += array[i]

# O(n²)
# Ω(n)
