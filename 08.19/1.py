from random import randint


class Generator:
    @staticmethod
    def generate(count: int):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    @staticmethod
    def split(array) -> list:
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    @staticmethod
    def verify(arrays) -> bool:
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    """Фасад, в котором собраны каждый экземпляр калссов"""
    def __init__(self):
        self.g = Generator()
        self.s = Splitter()
        self.v = Verifier()

    def gen(self):
        """Метод создающий квадрат определенного размера"""
        a, b, c = self.g.generate(3), self.g.generate(3), self.g.generate(3)
        matrix = self.s.split([a, b, c])
        return matrix

    def check(self):
        """Проверка реализации магического квадрата"""
        return self.v.verify(self.gen())

        # СДЕЛАТЬ: реализовать простой интерфейс для сборки и проверки магического квадрата


a = MagicSquareGenerator()
print(a.gen())
print(a.check())
