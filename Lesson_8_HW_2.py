class Error(Exception):
    def __init__(self, num_err):
        self.num = num_err

while True:

    num_1 = input("Введите, что делим: ")

    num_2 = input("Введите, на что делим: ")

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_2 == 0:
            raise Error("Делить на 0 нельзя")
    except ValueError:
        print("Вы ввели не число")
    except Error as err:
        print(err)
    else:
        print(f'{num_1} разделить на {num_2} равно {num_1 / num_2}')
        break
