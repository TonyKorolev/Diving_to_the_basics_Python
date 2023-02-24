# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

# преобразование умножения чисел и их результата в строку
def change_to_string_multiplication(a, b):
    result = a * b
    if result < 10:
        string_multiplication = f'{a} x {b} =  {a * b}' # перед результатом умножения два пробела
    else:
        string_multiplication = f'{a} x {b} = {a * b}' # перед результатом умножения один пробел
    return string_multiplication

# напечатать половину таблицы умножения
def write_half_of_table_multiplication(arr_nums):
    for i in range (2, 10):
        print(change_to_string_multiplication(arr_nums[0], i), change_to_string_multiplication(arr_nums[1], i), \
            change_to_string_multiplication(arr_nums[2], i), change_to_string_multiplication(arr_nums[3], i), sep='     ')
    if arr_nums[3] == 5:
        print('')

# напечатать полную таблицу умножения
def write_table_multiplicaton():
    write_half_of_table_multiplication(arr_nums=[2, 3, 4, 5])
    write_half_of_table_multiplication(arr_nums=[6, 7, 8, 9])

# программа
write_table_multiplicaton()
