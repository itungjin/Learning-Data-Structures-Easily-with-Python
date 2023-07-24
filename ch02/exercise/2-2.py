# 등차수열
# 양의 정수 n에 대한 함수 seq()의 호출 횟수

def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3

# 함수 seq()는 n회 호출된다.
