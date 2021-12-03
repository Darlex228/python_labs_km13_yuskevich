from string import ascii_lowercase

rd = open("gadsby.txt", "r")
f = rd.read().lower()
count = 0
list = []
def cnt(letter):
    count = 0
    for i in f:
        if i == letter:
            count += 1
    return count
def cnt_print(letter):
    cnt(letter)
    a = round(((cnt(letter) / 212115) * 100), 3)
    list.append(a)
    list.sort(reverse=True)


for i in ascii_lowercase:
    cnt_print(i)
for i in range(0, 5):
    for q in ascii_lowercase:
        if round(((cnt(q) / 212115) * 100), 3) == list[i]:
            print(q, list[i])
print('...')
for i in range(21, 26):
    for q in ascii_lowercase:
        if round(((cnt(q) / 212115) * 100), 3) == list[i]:
            print(q, list[i])

