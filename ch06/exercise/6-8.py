fib_call = [0] * 51
fib_call[1], fib_call[2] = 1, 1
for i in range(2, 51):
    fib_call[i] = 1 + fib_call[i-2] + fib_call[i-1]
print(fib_call[50])
