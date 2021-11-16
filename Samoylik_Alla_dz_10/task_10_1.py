class Matrix:
    def __init__(self, matrix):
        self.lines = matrix

    def __str__(self):
        matrix_list = []
        for line in self.lines:
            line_list = (str(el) for el in line)
            matrix_list.append(' '.join(line_list))
        return str('\n'.join(matrix_list))

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.lines)):
            new_line = list(map(sum, zip(self.lines[i], other.lines[i])))
            new_matrix.append(' '.join(str(el) for el in new_line))
        return str('\n'.join(new_matrix))


matrix_1 = Matrix([[1, 2, -3, 4], [5, 6, 7, -8]])
matrix_2 = Matrix([[12, 14, 25, 27], [33, -34, 17, 21]])

print(matrix_1, '\n')
print(matrix_2, '\n')
print(f'Сумма матриц \n{matrix_1 + matrix_2}')
