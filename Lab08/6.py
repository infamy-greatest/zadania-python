def fib(num):
    if num in [0, 1]:
        return num
    else:
        return fib(num - 2) + fib(num - 1)


print(fib(5))
