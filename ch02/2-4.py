# 하노이 탑

def move(n, a, b, c):
    if n > 0:
        move(n-1, a, c, b)
        print(str(a) + '에 있는 원판을 ' + str(b) + '로 옮긴다.')
        move(n-1, c, b, a)
