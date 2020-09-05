class Error():

    @staticmethod
    def inn_input():
        list = []
        while True:
            try:
                num_1 = input("Введите число или введите quit чтобы закончить: ").upper()
                if num_1 == "QUIT":
                    print(f'Вы введи: {list}')
                    break
                else:
                    num_2 = int(num_1)
                    list.append(int(num_2))
                    print(list)
            except ValueError:
                print("Вы ввели не число и не команду для выхода")

err = Error()
err.inn_input()