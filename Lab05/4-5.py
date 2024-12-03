num = int(input("Podaj liczbę dodatnią: "))
sum = 0
i = 1

while sum < num:
    i += 1
    sum += i
    print(sum)
    print(i)
i -= 1

print(f'Liczba pierwsyzch liczb dodatkich, których suma nie przekracza {num} wynosi {i}.')