num_words_in_dict = int(input())
dict = set()
for some_word in range(num_words_in_dict):
    dict.add(input().strip().lower())
num_strings = int(input())
list_of_strings = []
for some_string in range(num_strings):
    list_of_strings += (input().strip().lower().split(' '))

set_of_verif_words = (set(list_of_strings))

for some_word in set_of_verif_words:
    if some_word not in dict:
        print(some_word)

"""Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, 
после чего на d строках указываются эти слова. Затем передаётся количество l строк текста для проверки, 
после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
"""