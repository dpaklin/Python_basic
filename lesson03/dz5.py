# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.


def my_sum():
    exit_key = False
    result = 0
    while exit_key == False:
        my_list = input('Введите числа в строку или введите "Q" для выхода: ').split()
        summ = 0
        for i in my_list:
            if 'q' in i:
                exit_key = True
                break
            summ += int(i)
        result += summ
        print(f'Сумма чисел: {result}')


my_sum()