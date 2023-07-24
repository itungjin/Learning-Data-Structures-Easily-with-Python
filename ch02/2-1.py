# 등차수열

def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3
