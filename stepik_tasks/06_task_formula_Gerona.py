
# В то далёкое время, когда Паша ходил в школу, ему очень не нравилась
# формула Герона для вычисления площади треугольника, так как казалась
# слишком сложной. В один прекрасный момент Павел решил избавить всех
# школьников от страданий и написать и распространить по школам программу,
# вычисляющую площадь треугольника по трём сторонам.

# Одна проблема: так как эта формула не нравилась Павлу, он её не
# запомнил. Помогите ему завершить доброе дело и напишите программу,
# вычисляющую площадь треугольника по переданным длинам трёх его сторон по
# формуле Герона.

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c))
print(pow(S, 0.5))
