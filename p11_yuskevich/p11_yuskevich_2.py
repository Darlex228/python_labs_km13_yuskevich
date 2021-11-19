# ВАШ КОД ТУТ
def rrange(begin, end, step = None):
    count = 0
    if step != None:
        return list(range(begin, end, step))
    else:
        return list(range(begin, end))
            


# ПЕРЕВІРКА

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
#print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')