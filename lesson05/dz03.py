# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('txt/file5_3.txt', encoding='utf-8') as f_obj:
    sal = []
    poor = []
    my_list = f_obj.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {round((sum(map(float, sal)) / len(sal)), 2)}')
