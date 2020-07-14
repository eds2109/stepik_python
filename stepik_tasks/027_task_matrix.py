
# Дополнительная
# Выведите таблицу размером n x n, заполненную числами от 11 до n**2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке,
# как показано в примере (здесь n=5n=5):

n = int(input())
matrix = [[0] * n for i in range(n)]
c0 = 0
c1 = 1
matrix[n // 2][n // 2] = n * n
for v in range(n // 2):
    for i in range(n - c0):
        matrix[v][i + v] = c1
        c1 += 1
    for i in range(v + 1, n - v):
        matrix[i][-v - 1] = c1
        c1 += 1
    for i in range(v + 1, n - v):
        matrix[-v - 1][-i - 1] = c1
        c1 += 1
    for i in range(v + 1, n - (v + 1)):
        matrix[-i - 1][v] = c1
        c1 += 1
    c0 += 2
for i in matrix:
    print(*i)
