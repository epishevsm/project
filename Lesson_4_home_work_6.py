from itertools import count
from itertools import cycle

for el in count(1):
    if el > 10:
        break
    print(el)
a = ""
b = []
с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    # print(el)
    b.append(el)
    с += 1
a = ''.join(b)
print(a)
print(b)