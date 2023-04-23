import random


class Matrix:

    def __init__(self, m: int):
        self.m = m
        matrix = []
        for i in range(self.m):
            matrix.append([0] * self.m)

        for i in range(self.m):
            for j in range(self.m):
                matrix[i][j] = random.randint(1, 10)
        self.m = matrix

    def print(self):
        for i in range(len(self.m)):
            print(self.m[i])

    def add_matrix(self, other):
        result = []
        numbers = []
        if len(self.m) != len(other.m[0]):
            return 'Матрицы разного размера'
        else:
            for i in range(len(self.m)):

                for j in range(len(self.m[0])):
                    res = self.m[i][j] + other.m[i][j]
                    numbers.append(res)
                    if len(numbers) == len(self.m):
                        result.append(numbers)
                        numbers = []
        return result

    def multiply_matrix(self, other):
        result = []
        numbers = []
        if len(self.m) != len(other.m[0]):
            return 'Матрицы не согласованы'
        else:
            for i in range(len(self.m)):

                for j in range(len(self.m[0])):
                    res = self.m[i][j] * other.m[i][j]
                    numbers.append(res)
                    if len(numbers) == len(self.m):
                        result.append(numbers)
                        numbers = []
        return result



matrix_one = Matrix(6)
matrix_two = Matrix(6)
matrix_one.print()
print()
matrix_two.print()
print(matrix_one == matrix_two)
matrix_add = matrix_one.add_matrix(matrix_two)
print(matrix_add)
matrix_mult = matrix_one.multiply_matrix(matrix_two)
print(matrix_mult)