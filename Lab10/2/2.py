import time
i = 0

while i < 30:
    print(i)
    i += 1
    time.sleep(2 - (0.7 + (0.04 * i)))
