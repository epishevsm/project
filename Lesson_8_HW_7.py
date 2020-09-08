class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):

        if self.b + other.b > 0:
            return f'Сумма z1 и z2 равна = {self.a + other.a}+{self.b + other.b}i'
        else:
            return f'Сумма z1 и z2 равна = {self.a + other.a}{self.b + other.b}i'

    def __mul__(self, other):
        if self.b + other.b > 0:
            return f'Произведение z1 и z2 равно = {(self.a * other.a) - (self.b * other.b)}{(self.a * other.b) + (self.b * other.a)}i'
        else:
            return f'Произведение z1 и z2 равно = {(self.a * other.a) - (self.b * other.b)}+{(self.a * other.b) + (self.b * other.a)}i'

    def __str__(self):
        if self.b < 0:
            return f'z = {self.a}{self.b}i'
        else:
            return f'z = {self.a}+{self.b}i'


z_1 = ComplexNumber(1, 2)
z_2 = ComplexNumber(-5, 1)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)