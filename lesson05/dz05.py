# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('txt/file5_5.txt', 'w+') as f_obj:
    line = input('введите числа через пробел: ')
    f_obj.writelines(line)
    numbers = line.split()
    print(sum(map(int, numbers)))