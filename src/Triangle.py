from math import sqrt
from Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.name = Triangle

        @staticmethod
        def is_valid(a, b, c):
            return a + b > c and b + c > a and a + c > b


    # def area(self):
    #     return 100 + super().perimeter()

a = Triangle(2, 3, 4)
print(a.name)
print(a.area)
print(a.perimeter)