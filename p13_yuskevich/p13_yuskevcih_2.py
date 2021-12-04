m = {}
fm = {}

for i in range(1880, 2020):
    s = 'yob' + str(i) + '.txt'
    f = open(s, 'r')
    max_m = 0
    max_fm = 0

    for j in f:
        j = j.split(',')
        name = j[0]
        sex = j[1]
        amount = int(j[2])
        if sex == 'M':
            max_m = max(max_m, amount)
        if sex == 'F':
            max_fm = max(max_fm, amount)
    f = open(s, 'r')
    for u in f:
        u = u.split(',')
        name = u[0]
        sex = u[1]
        amount = int(u[2])
        if amount == max_m and sex == 'M':
            m[name] = m.get(name, 0) + 1

        if amount == max_fm and sex == 'F':
            fm[name] = fm.get(name, 0) + 1
    f.close()
m = sorted(m.items(), key=lambda h: h[1], reverse=True)
fm = sorted(fm.items(), key=lambda h: h[1], reverse=True)
for i in m:
    print(i[0], i[1])
print('-------------------------------------')
for i in fm:
    print(i[0], i[1])
