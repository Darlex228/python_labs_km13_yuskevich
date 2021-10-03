print("Введіть кількість хвилин")
min = int(input())        #amount of time in call
if min < 0:
    print("Кількість хвилин не може бути від'емним значенням")
elif 0 < min <= 50:
    print("100 grn")
elif 50 < min <= 100:
    print('150 grn')
elif 100 < min:
    print(2 * (min - 100) + 150, "grn")