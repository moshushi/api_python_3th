class Figure:
    def __init__(self,  *args):
        if len(args) < 1:
            raise ValueError ("Количество аргументов меньше 1")
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
        sum = 0
        for i in self.args:
          sum += i
        return sum

    @property
    def area(self):
        return None

    def add_area(figa):
        if not issubclass(figa, Figure):
            return ValueError("Добавляемый объект не фигура")
        return figa

# # a = Figure()
# a = Figure(name='Triangle')
# b = Figure('Triangle', 1, 2, 3)
# # a.name = 'Triangle'
# print(a.name)
# print(a.perimeter)
# print(b.name)
# print(b.perimeter)
d = Figure(1)
print(d.name)
print(d.perimeter)
print(d.area)
d.area = 10
print(d.area)
# e = Figure()
