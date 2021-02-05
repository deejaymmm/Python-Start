symb_to_crypt = input()
symb_to_decrypt = input()
word_to_crypt = input()
word_to_decrypt = input()
crypted_word = ''
decrypted_word = ''
dict_to_crypt = {}
dict_to_decrypt = {}
for i in range(0, len(symb_to_crypt)):
    dict_to_crypt[symb_to_crypt[i]] = symb_to_decrypt[i]
for i in range(0, len(symb_to_decrypt)):
    dict_to_decrypt[symb_to_decrypt[i]] = symb_to_crypt[i]
for i in range(0, len(word_to_crypt)):
    crypted_word += dict_to_crypt[word_to_crypt[i]]
for i in range(0, len(word_to_decrypt)):
    decrypted_word += dict_to_decrypt[word_to_decrypt[i]]
print(crypted_word)
print(decrypted_word)

"""Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba"""
