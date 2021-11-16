class Cell:
    def __init__(self, numb_of_cells):
        self.numb_of_cells = int(numb_of_cells)

    def __add__(self, other):
        common_cell = self.numb_of_cells + other.numb_of_cells
        return common_cell

    def __sub__(self, other):
        if self.numb_of_cells - other.numb_of_cells > 0:
            return self.numb_of_cells - other.numb_of_cells
        else:
            return f'Разность ячеек </= 0 --> Операция невозможна'

    def __mul__(self, other):
        common_cell = self.numb_of_cells * other.numb_of_cells
        return common_cell

    def __floordiv__(self, other):
        common_cell = self.numb_of_cells // other.numb_of_cells
        return common_cell

    def make_order(self, cells_in_row):
        self.cells_in_row = cells_in_row
        rows = ('*' * self.cells_in_row for i in range(self.numb_of_cells // self.cells_in_row))
        last_row = '*' * (self.numb_of_cells % self.cells_in_row)
        return '\n'.join(rows) + '\n' + last_row


cell_1 = Cell(18)
cell_2 = Cell(4)
cell_3 = Cell(23)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 - cell_3)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(f'\nОрганизация ячеек по рядам \n{cell_1.make_order(5)}')
