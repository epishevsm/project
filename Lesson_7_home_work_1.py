import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        sum_m = np.array(self.matrix) + np.array(self.matrix)
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in sum_m]))

    def __str__(self):
        return str(f'Сложение матриц: (\n{self.matrix})')


neo_1 = Matrix([[2, 2], [3, 3], [4, 4]])

neo_2 = Matrix([[2, 2], [3, 3], [4, 4]])

print(neo_1 + neo_2)
