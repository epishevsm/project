try:
    with open("text_3.txt", "r", encoding="utf-8") as home_w_3:
        salary = []
        low_sal = []
        list = home_w_3.read().split("\n")
        # print(list)
        for el in list:
            el = el.split()
            # print(el)
            if float(el[1]) < 20000.0:
                # print(el)
                low_sal.append(el[0])
            salary.append(el[1])
    print(f'Средняя зарплата сотрудника: {sum(map(float, salary)) / len(salary)}')
    print(f'Сотрудники с зарплатой ниже 20 000.0: {", ".join(low_sal)}.')


except IOError:
    print("Ошибка ввода-вывода")