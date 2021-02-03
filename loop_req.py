import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
r = requests.get(url.strip())
t = r.text

while True:
    url = t
    print(url)
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + url.strip())
    t = r.text
    if t[0:2] == 'We':
        print(t)
        break
print(t)

"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание."""