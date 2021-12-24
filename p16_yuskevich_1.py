def reg(active=True):
    def wrap(func):
        def wrapper(*args, **kwargs):

            if active:
                book = func(*args, **kwargs)
                new_book = []
                for i in book:
                    co_book = []
                    for j in range(4):
                        co_book.append((i[4*j], i[4*j+1], i[4*j+2], i[4*j+3]))
                    new_book.append(co_book)
                return new_book
            else:
                return func(*args, **kwargs)
        return wrapper
    return wrap


def copybook(n):
    nb = [16, 1, 2, 15, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]
    for i in range(16):
        nb[i] += 16 * n
    return nb


@reg(active=True)
def count(n):
    book = []
    for i in range(int(n/16)):
        book.append(copybook(i))
    return book


def work():
    while True:
        sheets = input('Введіть кількість сторінок книги (не більше 1280): ')
        if sheets.isdigit():
            sheets = int(sheets)
            if 0 < sheets <= 1280:
                if sheets % 16 != 0:
                    continue
                else:
                    for i in count(sheets):
                        print(i)
                    print('Кількість зошитів:', len(count(sheets)))
                    break
            else:
                continue
        else:

            continue


work()


while True:
    a = input('Якщо бажаєте повторити, напишіть "Так", якщо ні то введіть щось інше: ')
    if a.lower() == 'так':
        work()
    else:
        exit()
