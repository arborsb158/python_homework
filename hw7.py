class Matrix:
    def __init__(self, list_list):
        self.list_list = list_list

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.list_list])

    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.list_list)):

            for j in range(len(self.list_list[0])):
                result[i][j] = self.list_list[i][j] + other.list_list[i][j]

        return result


lst = Matrix([[2, 4, 6], [9, 8, 7], [4, 5, 6]])
lst2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(lst)
print(lst + lst2)

################################################################

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)

#############################################################################

class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nucleus // rows)]) + '\n' + '*' * (self.nucleus % rows)

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus - other.nucleus > 0:
            return Cell(self.nucleus - other.nucleus)
        else:
            return 'Разница количества ячеек двух клеток меньше нуля'

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __str__(self):
        return f'{self.nucleus}'


cell_1 = Cell(5)
cell_2 = Cell(6)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_2.make_order(5))
