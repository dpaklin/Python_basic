# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('txt/file5_4.txt', 'r', encoding='UTF-8') as file:
    nums = file.read().splitlines()
    i = 0
    list_num_rus = []
    for el in nums:
        el = el.split(' — ')
        for key, value in translate.items():
            if el[0] == key:
                el[0] = value
                list_num_rus.append(el[0] + ' — ' + el[1])


with open('txt/file5_4_ru.txt', 'w', encoding='utf-8') as f:
    for el in list_num_rus:
        f.write(el + '\n')

