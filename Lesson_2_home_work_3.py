seasons_list = ["зима", "весна", "лето", "осень"]
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month_list = ["январь", "ферваль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
              "декабрь"]
month_dict = {1: "январь", 2: "ферваль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябр", 10: "октябрь", 11: "ноябрь",
              12: "декабрь"}

user_month = None
while True:
    month = int(input("Введите число от 1 до 12: "))
    if month > 12 or month < 1:
        print("Вы ввели не верное число, введите число от 1 до 12: ")
    else:
        user_month = month
        break


if 1 <= user_month <= 2 or user_month == 12:
    print(seasons_dict.get(1))
    print(seasons_list[0])
    print(month_dict.get(month))
    print(month_list[user_month - 1])
elif 3 <= user_month <= 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
    print(month_dict.get(month))
    print(month_list[user_month - 1])
elif 6 <= user_month <= 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
    print(month_dict.get(month))
    print(month_list[user_month - 1])
else:
    print(seasons_dict.get(4))
    print(seasons_list[3])
    print(month_dict.get(month))
    print(month_list[user_month - 1])
