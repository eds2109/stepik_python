
# Напишите программу, которая получает на вход три целых числа, по одному
# числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.

# На ввод могут подаваться и повторяющиеся числа.

a, b, c = int(input()), int(input()), int(input())

if a >= b and a >= c:
    print(a)
elif b >= c and b >= a:
    print(b)
elif c >= a and c >= b:
    print(c)

if a <= b and a <= c:
    print(a)
elif b <= c and b <= a:
    print(b)
elif c <= a and c <= b:
    print(c)

if b <= a <= c or c <= a <= b:
    print(a)
elif a <= b <= c or c <= b <= a:
    print(b)
else:
    print(c)
