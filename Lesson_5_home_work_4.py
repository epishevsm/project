try:
    translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
    new_file = []
    with open('text_4.txt', 'r', encoding="utf-8") as home_w_4:
        for el in home_w_4:
            el = el.split(' ', 1)
            new_file.append(translate[el[0]] + '  ' + el[1].replace("\n", ""))
        print(new_file)
except IOError:
    print("Ошибка ввода-вывода")
