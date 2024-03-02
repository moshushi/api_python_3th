from math import sqrt
from Figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.name = Triangle
        self.a = a
        self.b = b
        self.c = c
        self.valid = self._is_valid

    @property
    def _is_valid(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise ValueError("Отрицательный аргумент")
        if self.a + self.b < self.c:
            raise ValueError("Не треугольник")
        if self.b + self.c < self.a:
            raise ValueError("Не треугольник")
        if self.a + self.c < self.b:
            raise ValueError("Не треугольник")
        return True

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        pol = self.perimeter / 2
        return sqrt(pol * (pol - self.a) * (pol - self.b) * (pol - self.c))

# a = Triangle(6, 8, 10)
# print(a.name)
# print(a.area)
# print(a.perimeter)
# b = Triangle(1, 2, 16)
# print(b.name)
# b._is_valid()
