import numpy as np

def get_year():
    year_lst = list(filter(lambda element: (element % 400 == 0) or (element % 100 != 0 and element % 4 == 0), years))
    return year_lst

years = np.arange(1900, 2020+1, 1)

def days(function, year, month):
    months = ('Январе', 'Феврале', 'Марте', 'Апреле', 'Мае', 'Июне', 'Июле',
              'Августе', 'Сентябре', 'Октябре', 'Ноябре', 'Декабре')
    days = ('31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31')
    if month == 2:
        year_list = function()
        if year in year_list:
            print('В {} {}-го 29 дней.'.format(months[1], year))
        else:
            print('В {} {}-го {} день/дней.'.format(months[1], year, days[1]))
    else:
        print('В {} {}-го {} день/дней.'.format(months[month-1], year, days[month-1]))

year = input('Введите год: ')
month = input('Введите месяц: ')
try:
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2020:
        print('Этот год находится вне указаных приделов')
    elif month <= 0 or month > 12:
        print('Такого месяца не существует')
    else:
        days(get_year, year, month)
except ValueError:
    print('Вы должны ввести цифры')