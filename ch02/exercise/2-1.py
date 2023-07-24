# 수열

def seq(n):
    if n == 1:
        return 0
    else:
        return 5 * seq(n-1) + 3

# 가상코드
# seq(n):
#     if (n=1) return 0
#     else return 5 * seq(n-1) + 3
