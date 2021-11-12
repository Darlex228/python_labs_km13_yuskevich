salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
a, b, c, d, e, f, g = 6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7
def mult(i):
    m = i * 0.3
    return[i, round(i + m, 2), round(m, 2)]
print(mult(a))
print(mult(b))
print(mult(c))
print(mult(d))
print(mult(e))
print(mult(f))
print(mult(g))