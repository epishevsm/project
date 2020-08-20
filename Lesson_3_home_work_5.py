def sum_of_num():
    sum_x = 0
    q = 0
    while q != "Q":
        user_str = input('Введите числа через пробел или введите Q для завершения: ').split()
        x = 0
        for el in range(len(user_str)):
            if user_str[el] == "q" or user_str[el] == "Q":
                q = "Q"
                break
            else:
                x = x + int(user_str[el])
        sum_x = sum_x + x
        print(f"Сумма чисел равна {sum_x}")
    print(f'Финальная сумма равна {sum_x}')

sum_of_num()