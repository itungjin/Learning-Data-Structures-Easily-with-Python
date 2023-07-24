# 하노이 탑
# move(5, a, b, c)를 호출할 때 원반을 옮기는 행위의 총 횟수

count = 0


def move(n, a, b, c):
    global count

    if n > 0:
        move(n-1, a, c, b)
        print(str(a) + '에 있는 원판을 ' + str(b) + '로 옮긴다.')
        count += 1
        move(n-1, c, b, a)


move(5, 'a', 'b', 'c')
print(count)

# 원반을 옮기는 행위의 총 횟수는 31
# move()의 총 호출 횟수는 원반을 옮기는 행위의 총 횟수에 2를 곱한 것에 1을 더한 것과 같다.
