from random import randint

n = 7
m = 10
b = []
for _ in range(m):
    a = []
    for _ in range(n):
        a.append(randint(0,20))
    b.append(a)

for _ in b:
    print("")
    for __ in _:
        if len(str(__)) == 2:
            print(f" {__}  ", end="")
        else:
            print(f"  {__}  ",end="")