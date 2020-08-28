try:
    with open('text_5.txt', 'w+', encoding="utf-8") as home_w_5:
        number = input("Введите числа через пробел: \n")
        home_w_5.writelines(number)
        list_num = number.split()
        print(sum(map(int, list_num)))
except IOError:
    print("Ошибка ввода-вывода")
except ValueError:
    print("Ошибка ввода-вывода")
(sum(map(int, number)))

