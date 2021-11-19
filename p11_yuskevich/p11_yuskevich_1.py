# ВАШ КОД ТУТ
def cons(head, tail = None):
    list_l = []
    list_l.append(head)
    if tail != None:
        list_l.extend(tail)
        return list_l
    return list_l

# ПЕРЕВІРКА

l = cons(3,
        cons(2,
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

# ПЕРЕВІРКА

#print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')