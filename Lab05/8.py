from random import randint

num = randint(1,100)
while True:
    chosen = int(input("Podaj liczbę całkowitą dodatnią w zakresie od 1-100: "))
    if chosen == num:
        print(f'Brawo, zgadłeś!')
        break
    else:
        print("Nieprawidłowa liczba, zgaduj dalej.")
