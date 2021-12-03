M = {}
F = {}

for i in range(1880, 2020):
    s = 'yob' + str(i) + '.txt'
    f = open(s, 'r')
    max_M = 0
    max_F = 0

    for j in f:
        j = j.split(',')
        name = j[0]
        sex = j[1]
        amount = int(j[2])
        if sex == 'M':
            max_M = max(max_M, amount)
        if sex == 'F':
            max_F = max(max_F, amount)
    f = open(s, 'r')
    for u in f:
        u = u.split(',')
        name = u[0]
        sex = u[1]
        amount = int(u[2])
        if amount == max_M and sex == 'M':
            M[name] = M.get(name, 0) + 1

        if amount == max_F and sex == 'F':
            F[name] = F.get(name, 0) + 1
    f.close()
M = sorted(M.items(), key=lambda h: h[1], reverse=True)
F = sorted(F.items(), key=lambda h: h[1], reverse=True)
for i in M:
    print(i[0], i[1])
print('-------------------------------------')
for i in F:
    print(i[0], i[1])