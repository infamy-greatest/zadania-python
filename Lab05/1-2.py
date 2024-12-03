def show_matrix(matrix):
    if isinstance(matrix, list):
        if isinstance(matrix[0], list) != True:
            print("Nieprawidłowa macierz.")
        else:
            for _ in matrix:
                for __ in _:
                    print(f' {__} ', end='')
                print("")
            print("")
    else:
        print("Nie jest to macierz.")


def transpose(matrix):
    transposed_matrix = []
    length = len(matrix[0])
    for _ in range(length):
        new_element = []
        for __ in matrix:
            new_element.append(__[_])
        transposed_matrix.append(new_element)
    return transposed_matrix


def transpose_using_while_loop(matrix):
    transposed_matrix = []
    for _ in range(len(matrix[0])):
        counter_index = 0
        new_element = []
        while counter_index != len(matrix):
            new_element.append(matrix[counter_index][0])
            counter_index += 1
        transposed_matrix.append(new_element)
        counter_index = 0
        while counter_index != len(matrix):
            matrix[counter_index].pop(0)
            counter_index += 1
    return transposed_matrix


def multiply_matrixes(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Błędna ilość kolumn i wierszy macierzy."
    matrix2 = transpose(matrix2)
    result = [[0 for _ in range(len(matrix2))] for _ in range(len(matrix1))]
    i = 0
    for _ in matrix1:
        for x in range(len(matrix2)):
            counter = 0
            sum = 0
            for __ in _:
                sum += __ * matrix2[x][counter]
                counter += 1
            result[i][x] = sum
        i += 1
    return result


A = [[1, 2, 3], [4, 5, 6]]                          # 3 kolumny, 2 wiersze
B = [[10, 11], [20, 21], [30, 31]]                  # 3 wiersze, 2 kolumny

show_matrix(A)
show_matrix(B)
show_matrix(multiply_matrixes(A, B))