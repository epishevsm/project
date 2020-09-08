class Storage:


    def __init__(self, storage_size):
        self.storage_size = int(storage_size)
        self.free_space = 0
        self.unit_count = 0
        self.all_unit_cost = 0
        self.in_storage = []
        self.out_storage = []



    def in_stor(self):
        try:

            while True:
                menu = input("Начать/продолжить введите --> Y, чтобы закончить введите --> N:  ").upper()
                if menu == "Y":
                    unit_name = input("Введите наименование устройства, например: 'принтер HP' -->  ")
                    unit_count = int(input("Введите колличество устройств-->  "))
                    unit_cost = int(input("Введите цену за одно устройство -->  "))
                    in_stor = {'Модель устройства': unit_name, 'Цена за ед': unit_cost, 'Количество': unit_count}
                    self.in_storage.append(in_stor)
                    self.all_unit_cost = self.all_unit_cost + unit_count * unit_cost
                    self.free_space = self.storage_size - unit_count
                    self.unit_count += 1
                elif menu == 'N':
                    return f'выход'
        except:
            f"ошибка ввода данных"

    def out_stor(self):
        try:

            department = input("Введите ваше подразделение -->  ")
            while True:
                menu = input("Начать/продолжить введите --> Y, чтобы закончить введите --> N:  ").upper()
                if menu == "Y":
                    for num, el in enumerate(self.in_storage):
                        num += 1
                        print(f'На складе осталось: {num}, {el}')
                    out_num = int(input("Узажите номер позиции которую Вы хотите забрать --> "))
                    out_count = int(input("Укажите сколько вы хотите забрать техники --> "))
                    self.in_storage[out_num-1]['Количество'] = self.in_storage[out_num-1]['Количество'] - out_count
                    out_stor = {'Подразделение': department, 'Цена за ед': self.in_storage[out_num-1]['Цена за ед'], 'Количество': out_count}
                    self.out_storage.append(out_stor)
                    self.free_space = self.free_space + out_count
                    self.all_unit_cost = self.all_unit_cost - out_count * self.in_storage[out_num-1]['Цена за ед']
                    print(self.all_unit_cost)
                elif menu == 'N':
                    return f'выход'
        except:
            f"ошибка ввода данных"

    def storage_status(self):
        try:
            type = input("Если хотите узнать что хнариться на складе введите 'in', если хотите узнать что и куда забрали со склада введите 'out' -->  ").upper()
            if type == "IN":
                return print('Каталог склада:\n',"\n ".join(str(el) for el in self.in_storage), "\nМеста на складе осталось: ", self.free_space, "\nПоставок на склад было: ", self.unit_count, f'\nЦенностей на складе на суммк: {self.all_unit_cost}')
            elif type == "OUT":
                return print(f"Со склада забрали: {self.out_storage}")
        except:
            return f'ввод цифр или иных символов не допустим'

class Office_equipment:

    def __init__(self, manufacturer, condition, objective):
        self.manufacturer = manufacturer
        self.condition = condition
        self.objective = objective

class Printer(Office_equipment):
    def __init__(self, manufacturer, condition, objective, paper_slot):
        super().__init__(manufacturer, condition, objective)
        self.paper_slot = paper_slot
    def __str__(self):
        return f'\n Производитель: {self.manufacturer}, Состояние: {self.condition}, Функционал: {self.objective}, Вместимость слота для бумаги: {self.paper_slot}\n'

class Scanner(Office_equipment):
    def __init__(self, manufacturer, condition, objective, scan_speed):
        super().__init__(manufacturer, condition, objective)
        self.scan_speed = scan_speed

    def __str__(self):
        return f' Производитель: {self.manufacturer}, Состояние: {self.condition}, Функционал: {self.objective}, Скорость работы: {self.scan_speed}\n'

class Xerox(Office_equipment):
    def __init__(self, manufacturer, condition, objective, size):
        super().__init__(manufacturer, condition, objective)
        self.size = size
    def __str__(self):
        return f' Производитель: {self.manufacturer}, Состояние: {self.condition}, Функционал: {self.objective}, Размер: {self.size}\n'


printer = Printer("HP", "new", "print", "200")
scanner = Scanner("Canon", "new", "scan", "20 copies per min")
xerox = Xerox("Xerox", "elder", "print and copy", "very very big")
print(printer)
print(scanner)
print(xerox)
storage = Storage(100)
print(storage.in_stor())
storage.out_stor()
storage.storage_status()
