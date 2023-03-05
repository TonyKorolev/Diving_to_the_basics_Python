# Напишите программу, которая получает целое число и 
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def enter_number():
    num = int(input("Enter number for decimal to hexadecimal conversion\n"))
    return num

def translateToABCDEF(num):
    if num == 10:
        stringABCDEF = 'A'
    elif num == 11:
        stringABCDEF = 'B'
    elif num == 12:
        stringABCDEF = 'C'
    elif num == 13:
        stringABCDEF = 'D'
    elif num == 14:
        stringABCDEF = 'E'
    elif num == 15:
        stringABCDEF = 'F'
    else:
        stringABCDEF = str(num)
    return stringABCDEF

def decimalToHexadecimalConversion(num):
    result = ''
    while num > 0:
        remainder_num = num % 16
        result = translateToABCDEF(remainder_num) + result
        num //= 16
    print(result)

number = enter_number()
decimalToHexadecimalConversion(number)
print(hex(number))