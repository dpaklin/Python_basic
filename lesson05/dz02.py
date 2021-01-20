# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('txt/file5_2.txt') as f:
    text = f.read().splitlines()

for index, value in enumerate(text):
        number_of_words = len(value.split())
        print('В строке {} есть {} слова.'.format(index + 1, number_of_words))
print('всего', len(text), 'строк(и)')
