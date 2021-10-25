while True:
    s1, s2 = str(input('Ведите первую строку: ')), str(input('Введите вторую строку: '))
    set1, set2 = set(), set()

    for i in s1:
        if i != ' ' and i.isalpha():
            set1.add(i.lower())
    for j in s2:
        if j != ' ' and j.isalpha():
            set2.add(j.lower())
    if len(set1) == 0 and len(set2) == 0:
        print('Вы должны ввести не только цифрв')
        continue
    flag = True
    for i in set2:
        if i in set1:
            continue
        else:
            print("Невозможно сформировать первую строку из второй")
            flag = False
            break
    if flag:
        print('Возможно создать новую строку')
    r = input('Если хотите попробовать еще введите "1", если нет то введите что угодно другое: ')
    if r == '1':
        continue
    else:
        break
