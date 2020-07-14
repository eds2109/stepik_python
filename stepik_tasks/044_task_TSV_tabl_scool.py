
# Дан файл с таблицей в формате TSV с информацией о росте школьников
# разных классов.

# Напишите программу, которая прочитает этот файл и подсчитает для каждого
# класса средний рост учащегося.

# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост

# Класс обозначается только числом. Буквенные модификаторы не
# используются. Номер класса может быть от 1 до 11 включительно. В фамилии
# нет пробелов, а в качестве роста используется натуральное число, но при
# подсчёте среднего требуется вычислить значение в виде вещественного
# числа.

# Выводить информацию о среднем росте следует в порядке возрастания номера
# класса (для классов с первого по одиннадцатый). Если про какой-то класс
# нет информации, необходимо вывести напротив него прочерк.

clses = [
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0}
]

with open("dataset_3380_5.txt", "r") as cls_file:
    for line in cls_file:
        line = line.split("\t")

        # Count a student anf his height
        clses[int(line[0]) - 1]["students"] += 1
        clses[int(line[0]) - 1]["height"] += int(line[2])

# Print info about each class, getting average height
for ind, cls in enumerate(clses):
    print("{} {:}".format(
        ind + 1, float(cls["height"]) /
        cls["students"] if cls["students"] else "-"
    ))
