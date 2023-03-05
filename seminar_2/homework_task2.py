# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions

# просим ввести дробное число
def enter_fractional_number(order):
    fractional_number_string = input(f'Enter {order} fractional number in "a/b" form\n')
    return fractional_number_string

# сплитуем дробное число
def selection_of_numerator_and_denominator(num_string):
    return num_string.split('/')

def check_whole_num(num1, num2):
    # выделение целого числа, если числитель больше знаменателя, и присутствует остаток от деления числителя на знаменатель
    # if num1 % num2 != 0 and num1 >= num2:
    #     result = f'{num1 // num2} {num1 % num2}/{num2}'
    # вывод целого числа, если числитель делиться на знаменатель без остатка
    # при добавлении условия выше в текущем заменить if на elif
    if num1 % num2 == 0:
        result = f'{int(num1 / num2)}'
    else:
        result = f'{num1}/{num2}'
    return result

# умножаем два дробных числа
def print_fractional_numbers_multiplication(num1_string, num2_string, num1_arr, num2_arr):
    numerator = int(num1_arr[0]) * int(num2_arr[0])
    denominator = int(num1_arr[1]) * int(num2_arr[1])
    result_string = check_whole_num(numerator, denominator)
    print(f'{num1_string} * {num2_string} = {result_string}')

# делим одно дробное число на другое
def print_fractional_numbers_division(num1_string, num2_string, num1_arr, num2_arr):
    numerator = int(num1_arr[0]) * int(num2_arr[1])
    denominator = int(num1_arr[1]) * int(num2_arr[0])
    result_string = check_whole_num(numerator, denominator)
    print(f'{num1_string} / {num2_string} = {result_string}')

# проверка с помощью модуля Fractions
def check_fractional_numbers_with_fractions_module(num1_arr, num2_arr):
    num1 = fractions.Fraction(int(num1_arr[0]), int(num1_arr[1]))
    num2 = fractions.Fraction(int(num2_arr[0]), int(num2_arr[1]))
    print('\n','Check results with Fractions module', sep='')
    print('Multiplication:', num1 * num2)
    print('Division:', num1 / num2)

# def check_fractional_numbers_division_with_fractions_module(num1_arr, num2_arr):
#     num1 = fractions.Fraction(num1_arr[0], num1_arr[1])
#     num2 = fractions.Fraction(num2_arr[0], num2_arr[1])
#     print(num1 / num2)

fractional_num1 = enter_fractional_number('first')
fractional_num2 = enter_fractional_number('second')
fractional_num1_arr = selection_of_numerator_and_denominator(fractional_num1)
fractional_num2_arr = selection_of_numerator_and_denominator(fractional_num2)
print()
print_fractional_numbers_multiplication(fractional_num1, fractional_num2, fractional_num1_arr, fractional_num2_arr)
print_fractional_numbers_division(fractional_num1, fractional_num2, fractional_num1_arr, fractional_num2_arr)
check_fractional_numbers_with_fractions_module(fractional_num1_arr, fractional_num2_arr)


