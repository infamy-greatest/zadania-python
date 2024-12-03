def wyszukaj(towar, nazwa):
    for key1 in towar:
        if key1['nazwa'] == nazwa:
            print(f'Nazwa towaru: {key1['nazwa']}')
            print(f'Jednostka towaru: {key1['jednostka']}')
            print(f'Ilość towaru: {key1['ilosc']}')
            print(f'Cena towaru: {key1['cena']}')


def sumuj(towar, nazwa):
    for key1 in towar:
        if key1['nazwa'] == nazwa:
            print(f'Suma towaru wynosi: {key1['ilosc'] * key1['cena']}')


def sumuj_wszystko(towar):
    suma = 0
    for key in towar:
        suma += key['ilosc'] * key['cena']
    print(f'Suma Sum towarów wynosi: {suma}')


def dodaj(towar, nazwa, jednostka, ilosc, cena):
    nowy_produkt = {'nazwa': nazwa, 'jednostka': jednostka, 'ilosc': ilosc, 'cena': cena}
    towar.append(nowy_produkt)


def aktualizuj_ilosc(towar, nazwa, ilosc):
    for key in towar:
        if key['nazwa'] == nazwa:
            key['ilosc'] = ilosc


def filtr_jednostka(towar, jednostka):
    for key in towar:
        if key['jednostka'] == jednostka:
            print(key)


towarA = [{'nazwa': 'banan', 'jednostka': 'kg', 'ilosc': 10, 'cena': 3},
          {'nazwa': 'jabłko', 'jednostka': 'kg', 'ilosc': 16, 'cena': 2.5},
          {'nazwa': 'mąka pszenna', 'jednostka': 'op.', 'ilosc': 30, 'cena': 2.5},
          {'nazwa': 'mydło', 'jednostka': 'szt.', 'ilosc': 6, 'cena': 1.5},
          {'nazwa': 'jogurt naturalny', 'jednostka': 'szt.', 'ilosc': 20, 'cena': 1.5},
          {'nazwa': 'papier toaletowy 8 rolek', 'jednostka': 'op.', 'ilosc': 10, 'cena': 9}]

if __name__ == '__main__':

    # wyszukaj(towarA, "jabłko")

    # sumuj(towarA, "jabłko")

    # sumuj_wszystko(towarA)

    # dodaj(towarA, "pomidor", "szt.", 20, 3.1)
    # wyszukaj(towarA, 'pomidor')

    # aktualizuj_ilosc(towarA, 'jabłko', 103)
    # wyszukaj(towarA, 'jabłko')

    filtr_jednostka(towarA, 'szt.')
