dict_a = {1: 10, 2: 20, 3: 30, 4: 40}
dict_b = {1: 11, 3: 33, 5: 55}
merged = {}
for keya, valuea in dict_a.items():
    for keyb, valueb in dict_b.items():
        if keya == keyb:
            merged[keya] = valuea + valueb

print(merged)

