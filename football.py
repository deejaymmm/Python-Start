def parce(com, res):
    for k in range(0, len(b)):
        if com in b[k]:
            if res == 3:
                b[k][2] += 1
            elif res == 1:
                b[k][3] += 1
            elif res == 0:
                b[k][4] += 1
            b[k][1] += 1
            b[k][5] += res
            break

n = int(input())
a = []
b = []
for i in range(n):
    a.append([j for j in input().strip().split(';')])
for i in range(n):
    if [a[i][0], 0, 0, 0, 0, 0,] not in b:
        b.append([a[i][0], 0, 0, 0, 0, 0,])
    if [a[i][2], 0, 0, 0, 0, 0,] not in b:
        b.append([a[i][2], 0, 0, 0, 0, 0,])

for i in range(n):
    if int(a[i][1]) > int(a[i][3]):
        parce(a[i][0], 3)
        parce(a[i][2], 0)
    elif int(a[i][1]) == int(a[i][3]):
        parce(a[i][0], 1)
        parce(a[i][2], 1)
    elif int(a[i][1]) < int(a[i][3]):
        parce(a[i][0], 0)
        parce(a[i][2], 3)

for i in range(0, len(b)):
    for j in range(0, 6):
        if j == 0:
            print(b[i][j], end=':')
        else:
            print(b[i][j], end=' ')
    print()

"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6"""