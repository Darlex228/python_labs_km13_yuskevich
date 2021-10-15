f = True

numb = {
    '1': ('.', ',', '?', '!', ':'),
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z'),
    '0': ' '
}

def key_val(val):
    for K, V in numb.items():         # Цикл который ищит кнопку в соответствии с введенным значением
        for J in V:
            if J == val:
                return K, V.index(j)


while f:
    print('Введите сообщение состоящие из букв:')
    sent = str(input())    # sent - sentence
    phone_var = ''
    for i in range(len(sent)):
        key, times = key_val(sent[i].upper())     # получение кнопки и индекса каждого символа в строке
        if key is not None:
            phone_var += str(key)*(times+1)
    if len(phone_var) == 0:          # проверка длины
        print('Вы ничего не ввели')

    else:
        print('то, как это выглядело бы на телефоне:')
        print(phone_var)
    print('Введите 1 если хотите повторить или же другой знак если нет')
    repeat = input()
    if repeat == '1':
        f = True
    else:
        print('Конец работы программы')
        break
