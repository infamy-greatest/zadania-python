from math import sqrt
def odleglosc (P1, P2):
    distancex = abs(P2[0] - P1[0])
    distancey = abs(P2[1] - P1[1])
    return sqrt(distancex*distancex + distancey*distancey)

punkt1 = [0, 0]
punkt2 = [3, 4]

print(odleglosc(punkt1, punkt2))
