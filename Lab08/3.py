def factorial(num):
    sumsum = 1
    for _ in range(1, num + 1):
        sumsum *= _
    return sumsum


print(factorial(5))
