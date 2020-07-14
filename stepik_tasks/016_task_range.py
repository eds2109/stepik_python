
# Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd,
# каждое в своей строке. Программа должна вывести фрагмент таблицы
# умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка
# [c;d][c;d].

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for r1 in range(c, d + 1):
    print('\t', str(r1), end='')
print()
for r2 in range(a, b + 1):
    print(str(r2), '\t', end='')
    for r3 in range(c, d + 1):
        print(str(r2 * r3), end='\t')
    print()
