subj = {}
with open('text_6.txt', 'r',encoding="utf-8") as home_w_6:

    for el in home_w_6:
        x = el.replace("-", '0').replace("(пр)", '').replace("(л)", '').replace("(лаб)", '').replace(":", "")
        print(x)
        sub, lect, pract, lab = x.split()
        subj[sub] = int(lect) + int(pract) + int(lab)
    print(f'Общее количество часов - {subj}')
with open('text_6.txt', 'r',encoding="utf-8") as home_w_6:
    dict = {}
    for el in home_w_6:
        subject, other = el.split(":")
        # print(subject)
        sum_other = sum(map(int, "".join([el for el in other if el == " " or (el >= "0" and el <= "9")]).split()))
        dict[subject] = sum_other
print(dict)