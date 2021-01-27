n = int(input())
a = [[0] * n for i in range(n)]
m = 1
k = n - 1
l = 0

while m < n ** 2 + 1:
    for i in range(l, k + 1):
        a[l][i] = m
        m += 1
        if m > n ** 2:
            break
    if m > n ** 2:
        break
    for i in range(n - k, k + 1):
        a[i][k] = m
        m += 1
        if m > n ** 2:
            break
    if m > n ** 2:
        break
    for i in range(k - 1, n - k - 2, -1):
        a[k][i] = m
        m += 1
        if m > n ** 2:
            break
    if m > n ** 2:
        break
    for i in range(k - 1, n - k - 1, -1):
        a[i][l] = m
        m += 1
        if m > n ** 2:
            break
    l += 1
    k -= 1

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()

"""Выведите таблицу размером n×n, заполненную числами от 1 до n^2 
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, 
  как показано в примере (здесь n=5):
  
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9"""