# fib(5)를 호출했을 때 fib()가 호출되는 횟수

count = 0


def fib(n):
    global count
    count += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib(5)
print(count)


# fib(1)을 호출했을 때 fib()는 1번 호출
# fib(2)을 호출했을 때 fib()는 1번 호출
# fib(3)을 호출했을 때 fib()는 3번 호출
# fib(4)을 호출했을 때 fib()는 5번 호출
# fib(5)을 호출했을 때 fib()는 9번 호출
