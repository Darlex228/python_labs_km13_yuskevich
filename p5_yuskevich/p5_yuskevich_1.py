salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
i = 0
print('Salary table:')
for i in range(0, 7):
    a = salary_list[i] / 100 * 30
    b = (salary_list[i] / 100 * 30) + salary_list[i]
    print(salary_list[i], round(b, 2), round(a, 2))

