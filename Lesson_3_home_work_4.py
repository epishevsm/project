def exponentiation(x, y):
    x = abs(x)
    if y > 0:
        y = y * -1
    return x**y
try:
    x = 0
    print(exponentiation(int(input("Введите цисло, которое будем возводить в степень: ")), int(input("Введите отрицательное цисло, которое будет являться отрицательной степенью: "))))
except ZeroDivisionError:
    print("Ноль не возводится в отрицательную степень")


def exponentiation(x, y):
    if y == 0:
        return 1
    return x*exponentiation(x, y -1)
num_1 = abs(int(input("Введите цисло, которое будем возводить в степень: ")))
num_2 = abs(int(input("Введите цисло, которое будет являться отрицательной степенью: ")))

negative_expt = 1 / exponentiation(num_1, num_2)
print(f"{num_1} в степени -{num_2} = {negative_expt}")
