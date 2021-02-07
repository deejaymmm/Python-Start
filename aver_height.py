out_list = []
for cur_out in range(1, 12):
    out_list.append([cur_out, 0, 0])
in_list = []
with open('input5.txt', encoding='utf8') as inf:
  for line in inf:
    in_list.append(line.strip().split('\t'))
for cur_in in range(len(in_list)):
    out_list[int(in_list[cur_in][0]) - 1][1] += 1
    out_list[int(in_list[cur_in][0]) - 1][2] += int(in_list[cur_in][2])

with open('output5.txt', 'w') as ouf:
    for cur_out in range(len(out_list)):
        if out_list[cur_out][2] == 0:
            ouf.write(str(out_list[cur_out][0]) + ' -\n')
        else:
            ouf.write(str(out_list[cur_out][0]) + ' ' + str(float(out_list[cur_out][2] / out_list[cur_out][1])) + '\n')

"""Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются. 
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, 
а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение 
в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса 
(для классов с первого по одиннадцатый). Если про какой-то класс нет информации, 
необходимо вывести напротив него прочерк.

В качестве ответа прикрепите файл с полученными данными о среднем росте.

Sample Input:

6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:

1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0"""