def fib(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    res = fib(num-1) + fib(num - 2)
    return res

for i in range(1, 10):
    print(fib(i))
