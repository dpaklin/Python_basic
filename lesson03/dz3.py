# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def sum_of_two_max(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(numbers))
    return sum(numbers)


print(sum_of_two_max(4, 66, 15))
