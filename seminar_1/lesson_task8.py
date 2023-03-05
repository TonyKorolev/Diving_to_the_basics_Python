# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

# печатаем пробелы
def write_spaces(count_spaces):
    string_spaces = ''
    for i in range (count_spaces):
        string_spaces += ' '
    return string_spaces

# печатаем звездочки
def write_stars(count_stars):
    string_stars = ''
    for i in range (2 * count_stars - 1):
        string_stars += '*'
    return string_stars

# рисуем елку
def image_fir_tree(number):
    count = 1
    while (count <= number):
        spaces = write_spaces(number - count)
        stars = write_stars(count)
        print(spaces+stars)
        count += 1

# программа
row_number = int(input("Enter the number of rows for fir tree image:\n"))
image_fir_tree(row_number)

