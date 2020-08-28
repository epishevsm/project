try:
    with open("text_2.txt", "r", encoding="utf-8") as home_w_2:
        content = home_w_2.readlines()
        print(f"Колличество строк в файле: {len(content)}")
    with open("text_2.txt", "r", encoding="utf-8") as home_w_2:
        content = home_w_2.readlines()
        for el in range(len(content)):
            print(f'Количестко слов в {el + 1}-ой строке: {len(content[el].split())}')


except IOError:
    print("Ошибка ввода-вывода")
