
# Напишите программу, которая считывает текст из файла (в файле может быть
# больше одной строки) и выводит самое частое слово в этом тексте и через
# пробел то, сколько раз оно встретилось. Если таких слов несколько,
# вывести лексикографически первое (можно использовать оператор < для
# строк).

with open("dataset_3363_3.txt", 'r+') as f:
    s = list(map(lambda i: i.strip('.,!?'), f.read().lower().split()))
    m = max(sorted(s), key=lambda j: s.count(j))
    print("%s %d" % (m, s.count(m)))