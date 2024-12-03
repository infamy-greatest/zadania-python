lista = []

while len(lista) < 10:
    try:
        user = int(input(f"Podaj liczbę ({len(lista) + 1} z 10): "))
        lista.append(user)
    except Exception:
        print("Błędne dane. ")

lista.reverse()

for _ in range(len(lista)):
    print(_)

print(max(lista))
