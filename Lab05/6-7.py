chosen_number = int(input("Podaj liczbę dodatnią: "))
num = 2
sum = 0

while num < chosen_number:
    for _ in range(2, int((num + 2)/2)):
        if num % _ == 0:
            break
    else:
        sum += 1
    num += 1
print(f'Istnieją {sum} liczby pierwsze mniejsze od liczby {chosen_number}')