from abc import ABC, abstractmethod

class Cloth(ABC):


    def __init__(self, size, height):
        self.size = size
        self.height = height

    def textile_for_coat(self):
        return f'необходимо ткани на польто: {round(self.size / 6.5 + 0.5, 2)}'

    def textile_for_suit(self):
        return f'необходимо ткани на костюм: {round(2 * self.height + 0.3, 2)}'
    @property
    def total_textile(self):
        self.total = round(self.size / 6.5 + 0.5 ,2) + round(2 * self.height + 0.3, 2)
        return f'Общее количество ткани: {self.total}'
    @abstractmethod
    def __str__(self):
        return f'Рост: {self.height}, Размер: {self.size}'

class Coat(Cloth):
    def __init__(self, size):
        self.size = size


    def __str__(self):
        return f'Размер: {self.size}'

class Suit(Cloth):
    def __init__(self, height):
        self.height = height


    def __str__(self):
        return f'Рост: {self.height}'

class Total(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):
        return f'Рост: {self.height}, Размер: {self.size}'


c = Coat(5)
s = Suit(1.8)
t = Total(5, 1.8)
print(c)
print(c.textile_for_coat())
print(s)
print(s.textile_for_suit())
print(t)
print(t.total_textile)