def alg_iterative(x, y):
    if 0 in (x, y):
        return 'Jesteś debilem.'
    while y != 0:
        x, y = y, (x % y)
    return x


def alg_recur(x, y):
    if y != 0:
        return alg_recur(y, (x % y))
    return x


num1 = 15
num2 = 6
divisor = alg_iterative(num1, num2)
print(divisor)
divisor = alg_recur(num1, num2)
print(divisor)