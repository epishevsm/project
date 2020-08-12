a = 10
b = 20
day = 1

while True:
    if a < b:
        print(f"{day}-й день: {round(a, 2)}")
        day += 1
        a = (a * 0.1) + a
    else:
        print(f"{day}-й день: {round(a, 2)}")
        break
print(f"На {day}-й день спортсмен достиг результата не менее {b} км. ")