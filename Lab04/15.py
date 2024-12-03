from random import randint

n = 4
m = 4
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

counter = 1
sum = 0
for _ in b:
    __ = _[counter:]
    sumsum = 0
    for ___ in __:
        sumsum += ___
    sum += sumsum
    counter += 1

print(f"\n \n {sum}")