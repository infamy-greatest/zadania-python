def sprawdz_uzytkownika(name):
    assert name['imie'] and name['wiek'], 'Niepoprawny obiekt'
    return "brak błędu"



uzytkownik1 = {"imie": "Anna", "wiek": 25}
uzytkownik2 = {"imie": "Piotr"}
print(sprawdz_uzytkownika(uzytkownik1)) # Brak błędu
print(sprawdz_uzytkownika(uzytkownik2)) # AssertionError: Niepoprawny obiekt
