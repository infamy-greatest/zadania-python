def oblicz_srednia(oceny):
    assert len(oceny) > 0, "Lista ocen nie może być pusta"
    return sum(oceny) / len(oceny)


# Przykład poprawny
print(oblicz_srednia([4, 5, 3])) # Wynik: 4.0
# Przykład z błędem
print(oblicz_srednia([])) # Zgłasza AssertionError: Lista ocen nie może być pusta
