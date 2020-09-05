class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def int_dd_mm_yy(cls, date):
        my_date = list(map(int, date.split('-')))
        return f'{my_date[0]}-{my_date[1]}-{my_date[2]} '

    @staticmethod
    def val(date):
        my_date = list(map(int, date.split('-')))
        if 1 <= my_date[0] <= 31:
            if 1 <= my_date[1] <= 12:
                if 1 <= my_date[2] <= 9999:
                    return print("Данные введены верно")
                else:
                    print("Не корректный год")
            else:
                print("Не корректный месяц")
        else:
            print("Не корректный день")


    def __str__(self):
        return self.date

date = Data('5-9-2020')
print(date)
print(date.int_dd_mm_yy('5-9-2020'))
print(Data.int_dd_mm_yy('5-9-2020'))
date.val('2-12-2020')
Data.val('2-13-2020')
