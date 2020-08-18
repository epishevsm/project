user_number = None
rating_list = [7, 5, 3, 3, 3, 2]
print(f"Это рейтинг, в который вы можете добавить число: {rating_list} \n")
i = 0

while user_number != "Q":
    user_number = input("Введите положительное число (чтобы выйти из программы введите 'q': ").upper()
    if user_number.isdigit() > 0:
        user_number = int(user_number)
        for el in rating_list:
            if user_number <= el:
                i += 1
        rating_list.insert(i, float(user_number))
        i = 0
        print(rating_list)
    elif not user_number.isdigit() > 0 and user_number != "Q":
        print("Ошибка")
    else:
        print("Выход")