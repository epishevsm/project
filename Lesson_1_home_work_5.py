profit = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if profit > costs:
    i = (profit - costs) / profit * 100
    print(f"Прибыль {i}%")
    staff = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на одного сотрудника {i / staff} ")
else:
    print(f"Убыток ")


