from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        if el > 10:
            break
        yield factorial(el)


for i in fibo_gen():
    print(i)
