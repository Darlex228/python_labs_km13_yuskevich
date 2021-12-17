import itertools

list1 = ['diamonds', 'clubs', 'hearts', 'spades']
list2 = ['A', *range(2, 11), 'J', 'Q', 'K']
gen = itertools.product(list1, list2)
it = iter(gen)
for i in range(len(list1)*len(list2)):
    a = next(it)
    print(a[1], a[0])
next(it)