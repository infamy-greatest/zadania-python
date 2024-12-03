dict1 = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2}
sumsum = 0
for key, value in dict1.items():
    if value % 2 != 0:
        sumsum += value

print(sumsum)
