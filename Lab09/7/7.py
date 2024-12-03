def permute(la, a, l, r):
    if l == r:
        la.append(a)
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(la, a, l+1, r)
            a[l], a[i] = a[i], a[l]


a = ['A', 'B', 'C']
lista = []
permute(lista, a, 0, len(a)-1)
print(lista)
