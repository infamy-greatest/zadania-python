import numpy

A = [[1, 2, 3], [4, 5, 6]]                          # 3 kolumny, 2 wiersze
B = [[10, 11], [20, 21], [30, 31]]                  # 3 wiersze, 2 kolumny

# Zadanie 3

A = numpy.transpose(A)
print(A)
A = numpy.transpose(A)

result = numpy.dot(A,B)
print (result)
