from math import sqrt
def odleglosc(p1, p2):
    distancex = abs(p2[0] - p1[0])
    distancey = abs(p2[1] - p1[1])
    return sqrt(distancex*distancex + distancey*distancey)


def oneline(p1, p2, p3):
    a1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    a2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
    if a1 == a2:
        return True
    else:
        return False

def obwod(p1, p2, p3):
    if oneline(p1, p2, p3) == False:
        od1 = odleglosc(p1, p2)
        od2 = odleglosc(p2, p3)
        od3 = odleglosc(p1, p3)
        return od1 + od2 + od3
    else:
        print("Punkty nie tworzą trójkąta. ")
        return 0


print(obwod([0, 3], [3, 6], [6, 9]))
print(obwod([-1, -30], [0, -20], [1, -10]))
print(obwod([7.5, -8], [-2, 0], [7, 12]))
