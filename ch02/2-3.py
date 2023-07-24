# 피보나치 수열(비재귀 버전)

def fib_fast(n):
    f = [0] * (n+1)
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
