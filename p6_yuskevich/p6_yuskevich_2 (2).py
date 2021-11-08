phone = {
         '1': ('.', ',', '?', '!', ':'),
         '2': ('a', 'b', 'c'),
         '3': ('d', 'e', 'f'),
         '4': ('g', 'h', 'i'),
         '5': ('j', 'k', 'l'),
         '6': ('m', 'n', 'o'),
         '7': ('p', 'q', 'r', 's'),
         '8': ('t', 'u', 'v'),
         '9': ('w', 'x', 'y', 'z'),
         '0': ' '}

while True:
    text = input('Введите текст: ')
    if len(text) == 0:
        print('вы должны что-то ввести')
    out = ''
    for i in text:
        for main, m in phone.items():
            for j in m:
                if j == i.lower():
                    out += main*(m.index(j)+1)
    print(out)
    res = str(input('Введите "да" если хотите повторить или что-то другое что б закончить: '))
    if res.lower() == 'да':
        continue
    else:
        break