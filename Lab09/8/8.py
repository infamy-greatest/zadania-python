def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    perms = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            perms.append([m] + p)
    return perms


print(permutation(['A', 'B', 'C']))

# ODPOWIEDŹ C
# jeśli w liście już nie ma żadnego elementu, no to zwróć [], czyli nic,
# oraz jeśli jest tylko jeden element to zwróć ten jeden element

# ODPOWIEDŹ D
# w perms są przechowywane wszystkie permutacje, a lst to lista, na której odbywa się rekurencja (działamy na niej)

# ODPOWIEDŹ E
# m jest potencjalnym pierwszym elementem listy
# remlst to remaining list, czyli jak m to A, to reszta to BC, a jak m to B, to będzie tylko C

# ODPOWIEDŹ F
# lst nigdy się nie zmienia, i w całkowitych 3 iteracjach to będzie kolejno 0, 1 i 2, a, czynnik m: kolejno A, B i C, a remlst BC AC i AB (nie uwzględniam dalszych rekurencji, tylko główne iteracje)

# ODPOWIEDŹ G
# ta pętelka po prostu zwraca wszystke permutacje w remlst