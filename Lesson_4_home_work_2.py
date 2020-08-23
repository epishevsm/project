list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for num, el in enumerate(list) if list[num - 1] < list[num] and num != 0]
print(new_list)
# Результат: [12, 44, 4, 10, 78, 123].