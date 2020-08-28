import json
import numpy as np

try:
    final_list = []
    with open('lesson_5_hw_7.json', 'w',encoding="utf-8") as json_hw_7:
        with open('text_7.txt', 'r',encoding="utf-8") as home_w_7:
            dict = {}
            for el in home_w_7:
                subject, other = el.split(" ", 1)
                other = other.split()
                sum_other = int(other[1]) - int(other[2])
                dict[subject] = sum_other
            average = np.mean([int(el) for el in dict.values() if int(el) > 0])
            final_list.append(dict)
            final_list.append({"Average": round(average)})
        print(final_list)
        json.dump(final_list, json_hw_7)
except IOError:
    print("Ошибка ввода-вывода")
except ValueError:
    print("Ошибка ввода-вывода")

