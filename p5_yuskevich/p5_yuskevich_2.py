import time



string = str(input("Пишите слова в строку: "))
el_list = list(string.split())

comma = len(el_list) - 2
comma_ins = 0
for i in range(len(el_list)):
    if comma_ins < comma:
        el_list[i] += ','
        comma_ins += 1
if len(el_list) != 1:
    el_list.insert(-1, 'and')

print(*el_list)


