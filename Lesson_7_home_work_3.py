class Cell:
    def __init__(self, num_of_cell):
        self.num_of_cell = int(num_of_cell)

    def __str__(self):
        return self.num_of_cell * "*"

    def __add__(self, other):
        return f'При сложении двух клетов получается {Cell(self.num_of_cell + other.num_of_cell)} ячеек'

    def __sub__(self, other):

        if (self.num_of_cell - other.num_of_cell) > 0:

            return f'При вычитании одной клетки из другой получается {Cell(self.num_of_cell - other.num_of_cell)} ячеек'
        else:
            return f'Отрицательное количество клеток'
        # return f'При вычитании одной клетки из другой получается {Cell(self.num_of_cell - other.num_of_cell)} клеток' if (self.num_of_cell - other.num_of_cell) > 0 else 'Отрицательное количество клеток!'

    def __mul__(self, other):
        return f'При умножении двух клетов получается {Cell(self.num_of_cell * other.num_of_cell)} ячеек'

    def __truediv__(self, other):
        return f'При делении двух клетов получается одна клетка с {Cell(round(self.num_of_cell // other.num_of_cell))} ячеек'


    def make_order(self, order):
        sum_m = ""
        for el in range(int(self.num_of_cell // order)):
            sum_m += f'{"*" * order}\n'
        sum_m += f'{"*" * (self.num_of_cell % order)}'
        return sum_m



cell_1 = Cell(23)
cell_2 = Cell(15)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))



