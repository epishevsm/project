from sys import argv

time, payment, bonus = argv


try:
    time = int(time)
    payment = int(payment)
    bonus = int(bonus)
    result = (time * payment) + bonus
    print(f"Проработано часов: {time}, ставка за час: {payment}, премия: {bonus} Ваша заработная плана составила {result}")
except ValueError:
    print("Вы ввели не число")

