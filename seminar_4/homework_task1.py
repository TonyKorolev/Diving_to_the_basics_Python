# Напишите функцию для транспонирования матрицы

def transposition_matrix(matrix: list):
    """This method is used for transposition matrix.
    
    Input data: matrix (two-dimensional array).

    Method returns the transposed matrix."""
    transposed_matrix = []
    transposed_matrix_rows = zip(*matrix)
    for row in transposed_matrix_rows:
        transposed_matrix.append(list((row)))
    return transposed_matrix

def print_matrix_by_rows(matrix: list):
    """This method is used for print matrix by rows"""
    for row in matrix:
        print(row)

matrix = [[54, 32, 5, 98],
          [87, 51, 24, 81],
          [11, 91, 65, 46],
          [74, 79, 3, 26]]
transposed_matrix = transposition_matrix(matrix)
print_matrix_by_rows(transposed_matrix)
# print(transposed_matrix)