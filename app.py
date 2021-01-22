s = input()
n = ''
j = s[0]
k = 0
for i in s:
    if i == j:
        k += 1
    else:
        n += j + str(k)
        k = 1
        j = i
n += j + str(k)
print(n)
