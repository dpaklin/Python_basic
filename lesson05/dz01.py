# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.

out_file = open('txt/file5_1.txt', 'w', encoding='utf-8')
while True:
    my_str = input('введите что-нибудь: ')
    if my_str == '':
        break
    out_file.writelines(my_str + '\n')
out_file.close()