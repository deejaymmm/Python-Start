nun_mov = int(input())
moves = []
coord_x = 0
coord_y = 0
for cur_mov in range(nun_mov):
    moves.append(input().strip().lower().split(' '))
    if moves[cur_mov][0] == 'север':
        coord_y += int(moves[cur_mov][1])
    elif moves[cur_mov][0] == 'запад':
        coord_x -= int(moves[cur_mov][1])
    elif moves[cur_mov][0] == 'юг':
        coord_y -= int(moves[cur_mov][1])
    elif moves[cur_mov][0] == 'восток':
        coord_x += int(moves[cur_mov][1])
print(coord_x, coord_y)

"""Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, 
а число после слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, 
что можно написать программу, которая определит, куда в итоге биологи приведут черепашку. 
Для этого программисты просят вас написать программу, которая выведет точку, 
в которой окажется черепашка после всех команд. Для простоты они решили считать, 
что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

Программе подаётся на вход число команд n, которые нужно выполнить черепашке, 
после чего n строк с самими командами. Вывести нужно два числа в одну строку: 
первую и вторую координату конечной точки черепашки. Все координаты целочисленные.

Sample Input:

4
север 10
запад 20
юг 30
восток 40
Sample Output:

20 -20"""