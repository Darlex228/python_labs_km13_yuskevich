def factorial(n):
    if n == 0:
        return True
    return n*factorial(n-1)
while True:
    a = input('Введіть натуральне число: ')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Ви ввели не число, повторіть ще раз')
        continue
for i in range(a + 1):
    gen = (factorial(i)/(factorial(j)*factorial(i-j)) for j in range(i + 1))
    it = iter(gen)
    for j in it:
        print(int(j), end=' ')
    print()
