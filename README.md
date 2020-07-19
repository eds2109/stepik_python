## Программирование на Python

Все решенные задания из онлайн курса - [Stepik программирование на Python](https://stepik.org/course/67/). 
 
Задания находятся в папке `/stepik_tasks/`. 
Названия файлов упорядочены в порядке возрастания заданий с примерным смысловым названием файлов.
Файлы имеют такой вид: 
`01_task_input_sleep.py`, `02_task_...`, `03_task_...` и так далее.

Стуктура самих файлов с заданиями имеют такой вид.
Вверху описания задания, внизу код с решением задачи.

### Пример.
'''
Требуется определить, является ли данный год високосным.

Напомним, что високосными годами считаются те годы, порядковый номер
которых либо кратен 4, но при этом не кратен 100, либо кратен 400
(например, 2000-й год являлся високосным, а 2100-й будет невисокосным
годом).

Программа должна корректно работать на числах 1900≤n≤3000.

Выведите "Високосный" в случае, если считанный год является високосным и
"Обычный" в обратном случае (не забывайте проверять регистр выводимых
программой символов).
'''

`
x = int(input())
if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
    print('Високосный')
else:
    print('Обычный')
`
