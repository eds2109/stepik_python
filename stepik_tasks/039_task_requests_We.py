
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".

# Скачайте предложенный файл. В нём содержится ссылка на первый файл из
# этого набора.

# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/

# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests

download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '699991.txt'

while filename:
    print(filename)
    r = requests.get(download_link + filename)
    filename = None if r.text.startswith('We') else r.text

print(r.text)
