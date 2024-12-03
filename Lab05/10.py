num = 23123
print(f'Liczba {num}', end='')
binary = ''
while num > 1:
    if num % 2 != 0:
        binary += '1'
    else:
        binary += '0'
    num = num // 2
if num == 1:
    binary += '1'
elif binary == '':
    binary += '0'
print(f' w systemie binarnym to {binary[::-1]}')