def super_funkcja_robiaca_pole_prostokata(a, b):
    assert a > 0 and b > 0, 'Wymiary muszą być dodatnie'
    return a * b


print(super_funkcja_robiaca_pole_prostokata(5, 10)) # Wynik: 50
print(super_funkcja_robiaca_pole_prostokata(-5, 10)) # AssertionError: Wymiary muszą być dodatnie
