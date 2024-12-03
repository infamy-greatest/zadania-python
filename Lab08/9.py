def factorize(num):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    if num in [1, 2]:
        if num == 2:
            return " 2"
        else:
            return ''
    else:
        return factorize(num//i) + f' {i}'


print(factorize(96))

