# 하노이 탑
# move(5, a, b, c)를 호출할 때 함수 move()가 호출되는 횟수

count = 0


def move(n, a, b, c):
    global count
    count += 1

    if n > 0:
        move(n-1, a, c, b)
        print(str(a) + '에 있는 원판을 ' + str(b) + '로 옮긴다.')
        move(n-1, c, b, a)


move(5, 'a', 'b', 'c')
print(count)

# move(0, a, b, c)를 호출할 때 move()는 1번 호출
# move(1, a, b, c)를 호출할 때 move()는 3번 호출
# move(2, a, b, c)를 호출할 때 move()는 7번 호출
# move(3, a, b, c)를 호출할 때 move()는 15번 호출
# move(4, a, b, c)를 호출할 때 move()는 31번 호출
# move(5, a, b, c)를 호출할 때 move()는 63번 호출
