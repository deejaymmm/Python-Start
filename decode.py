with open('input.txt') as inf:
  for s in inf:
    s = s.strip()
    print(s)

n = ''
k = ''
m = ''
for i in s:
  if i.isdigit():
    k += i
  elif k == '':
    m = i
  else:
    for j in range(0, int(k)):
      n += m
    k = ''
    m = i
for j in range(0, int(k)):
  n += m
print(n)

with open('output.txt', 'w') as ouf:
  ouf.write(n + '\n')

"""На прошлой неделе мы сжимали строки, используя кодирование повторов. 
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, 
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. 
В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". 
Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. 
Запустите вашу программу, используя этот файл в качестве входных данных. 
Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

Sample Input:

a3b4c2e10b1
Sample Output:

aaabbbbcceeeeeeeeeeb"""