class Figure:
    def __init__(self, *args):
        if len(args) < 1:
            raise ValueError("Количество аргументов меньше 1")
        self.name = "Figure"
        # self.area = None
        self.args = args

    # @property
    # def number_of_side(self, args):
    #     if len(args) < 1:
    #         raise ValueError("Количество аргументов меньше 1")
    #     return self._number_of_side

    @property
    def perimeter(self):
        summ = 0
        for i in self.args:
            summ += i
        return summ

    @property
    def area(self):
        return self.perimeter

    def add_area(self, figa):
        if not isinstance(figa, Figure):
            return ValueError("Добавляемый объект не фигура")
        return self.area + figa.area

# d = Figure(5)
# e = Figure(6)
# print(d.name)
# print(d.area)
# d.add_area(e)
# print(d.add_area(e))
