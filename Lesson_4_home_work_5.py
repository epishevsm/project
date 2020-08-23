from functools import reduce


list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Четные числа от 100 до 1000: \n {list} \n Умножение всех четных элементов списка: {reduce(lambda x, y: x * y, list)}")


