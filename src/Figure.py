class Figure:
    def __init__(self, a):
        self.name = Figure
        self.a = a
        self.valid = self._is_valid

    @property
    def _is_valid(self):
        if self.a < 0:
            raise ValueError("Отрицательный аргумент")
        return True

    @property
    def perimeter(self):
        return self.a

    @property
    def area(self):
        return self.a

    # @property
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            return ValueError("Переданный объект не фигура")
        return self.area + figure.area


# f = Figure(1)
# print(f.name)
# print(f.valid)
# print(f.perimeter)
# print(f.area)
# # e = Figure(-1)
# l = Figure(5)
# print(l.add_area(f))

