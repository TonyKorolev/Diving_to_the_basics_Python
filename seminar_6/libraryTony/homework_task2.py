# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.


"""Use this module for check right date.
"""


__all__ = ['check_date_is_right']


def check_date_only_num(arr: list) -> bool:
    """Method returns True if all elements of the accepted list are digit, otherwise False.
    """
    flag = True
    for item in arr:
        if not(item.isdigit()):
            flag = False
    return flag


def check_date_is_right(date: str) -> bool:
    """Method accepts date and returns True if date is right, otherwise False.
    """
    date_is_right = True
    arr_mm_30 = [4, 6, 9, 11]
    arr_date = date.split('.')
    if check_date_only_num(arr_date) == False:
        date_is_right = False
    if len(arr_date) != 3:
        date_is_right = False
    else:
        dd = int(arr_date[0])
        mm = int(arr_date[1])
        year = int(arr_date[2])
        print(dd, mm, year)
        if not(1 <= dd <= 31):
            date_is_right = False
        elif not(1 <= mm <= 12):
            date_is_right = False
        elif not(1 <= year <= 9999):
            date_is_right = False
        elif mm == 2 and dd == 29 and year % 4 == 0:
            date_is_right = True
        elif mm == 2 and dd > 29 and year % 4 == 0:
            date_is_right = False
        elif mm == 2 and dd >= 29 and year % 4 != 0:
            date_is_right = False
        elif mm in arr_mm_30 and dd == 31:
            date_is_right = False
        else:
            date_is_right = True
    return date_is_right
