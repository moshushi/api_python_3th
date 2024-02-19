class Figure:
    def __init__(self, name, *args):
        self.name = name
        self.area = None
        self.args = args

    @property
    def perimeter(self):
        sum = 0
        return sum(*self.args)

# a = Figure()
a = Figure(name='Triangle')
# a.name = 'Triangle'
print(a.name)
print(a.perimeter)