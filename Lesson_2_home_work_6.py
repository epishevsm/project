goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0

while True:
    if input("For exit enter 'Q', for contonue enter 'Y': ").upper() == 'Q':
        break
    num += 1
    for el in features.keys():
        ins_key = input(f'Введите параметр "{el}": ')
        #features[el] = int(ins_key) if (el == 'цена' or el == 'количество') else ins_key я не доконца понял, как эта строка работает, поэтому написал через  is и else
        if el == 'цена' or el == 'количество':
            features[el] = int(ins_key)
        else:
            features[el] = str(ins_key)
        analytics[el].append(features[el])
    goods.append((num, features))
    print(f'Текущая аналитика по товарам: \n')
    for key, value in analytics.items():
        print(f'{key}: {value}')




