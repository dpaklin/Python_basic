# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def my_func(name, surname, byear, city, email, phone):
    print(f'{name} {surname}, {byear}, {city}, {email}, {phone}')


my_func(name='Ivan', surname='Ivanov', byear=1982, city='Moscow', email='ii@mail.ru', phone='+79999999999')
