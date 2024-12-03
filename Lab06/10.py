from math import sqrt
def odleglosc(p1, p2):
    distancex = abs(p2[0] - p1[0])
    distancey = abs(p2[1] - p1[1])
    return sqrt(distancex*distancex + distancey*distancey)


def obwod(p1, p2, p3):
    od1 = odleglosc(p1, p2)
    od2 = odleglosc(p2, p3)
    od3 = odleglosc(p1, p3)
    return od1 + od2 + od3


print(obwod([0, 0], [0, 4], [3, 0]))
print(obwod([7.5, -8], [-2, 0], [7, 12]))
