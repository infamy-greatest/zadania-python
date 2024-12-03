from math import asin, sqrt, degrees


def find_hypotenuse(cathetus1, cathetus2):
    hypotenuse = sqrt(cathetus1**2 + cathetus2**2)
    return hypotenuse


def find_angles(a, b, c):
    angle1 = degrees(asin(a / c))
    angle2 = degrees(asin(b / c))
    angles = [round(angle1, 2), round(angle2, 2)]
    return angles


def main():
    a = 3.0
    b = 4.0
    c = find_hypotenuse(a, b)
    angles = find_angles(a, b, c)
    print(f'Długość przeciwprostokątnej wynosi: {c}')
    print(f'Kąty w tym trójkącie wynoszą odpowiednio {angles[0]} i {angles[1]} stopni.')


if __name__ == "__main__":
    main()
