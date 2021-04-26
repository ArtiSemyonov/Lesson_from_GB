class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        new_matrix = []
        for first_matrix_row, second_matrix_row in zip(
            self.matrix, other.matrix
        ):
            new_row = []
            for index in range(len(first_matrix_row)):
                sum_of_elements = \
                    first_matrix_row[index] + second_matrix_row[index]
                new_row.append(sum_of_elements)
            new_matrix.append(new_row)
        return Matrix(new_matrix)


m1 = Matrix([[1, 2, 3], [4, 5, 6, ], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6, ], [7, 8, 9]])
print(m1)
# Пустой принт для разделения матриц
print()
print(m2)
m3 = m1 + m2
print()
print(m3)
