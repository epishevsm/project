try:
    with open("Home_work_1.txt", "a", encoding="utf-8") as home_w_1:
        user_str = None
        while user_str != "":
            user_str = input("Введите то, что хотите записать в файл, если вы введете пустую строку ввод окончится: ")
            print(user_str, file=home_w_1)

except IOError:
    print("Ошибка ввода-вывода")
