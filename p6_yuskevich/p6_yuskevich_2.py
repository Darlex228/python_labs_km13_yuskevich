def make16(num):
    letters = tuple('a' 'b' 'c' 'd' 'e' 'f')
    if num == 0:
        return '00'
    string_def = ''
    while num > 0:
        if num % 16 >= 10:
            ind = (num % 16) - 10
            string_def += letters[ind]
        else:
            temp = str(num % 16)
            string_def += temp
        num = num // 16
    string_def = string_def[-1::-1]
    if len(string_def) == 1:
        string_def = '0' + string_def
    return string_def

r = input('Введите значение для красного цвета: ')
g = input('Введите значение для зеленого цвета: ')
b = input('Введите значение для синего цвета: ')

try:
    r = int(r)
    g = int(g)
    b = int(b)
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        string_r = make16(r)
        string_g = make16(g)
        string_b = make16(b)
        string = '#' + string_r + string_g + string_b
        print(string)
    else:
        print('Вы вышли за границы допустимых значений чисел')
except ValueError:
    print('вы должны ввести цифры')