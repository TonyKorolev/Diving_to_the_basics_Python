# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# тут я пытался по феншую сделать, но почему-то ошибку try не собирается ловить

# проверка, что введенные данные это числа
# def sides_of_triangle_is_digit(arr):
#     for i in range (len(arr)):
#         if arr[i].isdigit():
#             sidesIsDigit = True
#         else:
#             sidesIsDigit = False
#     return sidesIsDigit

# проверка на положительные числа
# def sides_of_triangle_is_positive_numbers(arr):    
#     try:
#         for i in range(len(arr)):
#             num = int(arr[i])
#             if num > 0:
#                 sidesIsPositveNumbers = True
#             else:
#                 sidesIsPositveNumbers = False
#                 print("Enter numbers is not positive")
#     except RuntimeError:
#         print("Enter numbers is not whole")
#     finally: sidesIsPositveNumbers = False
#     return sidesIsPositveNumbers

# проверка введенных данных, если не корректные, просим ввести еще раз
# def enter_sides_of_triangle_check():
#     flag = False
#     while(flag == False):
#         sides_of_triangle = input('Enter sides of triangle in format: "A B C", where A, B, C are whole positive numbers.\n')
#         arrSidesOfTriangle = sides_of_triangle.split(' ')
#         if sides_of_triangle_is_digit(arrSidesOfTriangle) == False:
#             print("Enter data is not numbers")
#             flag = False
#         else:
#             flag = True
#         if sides_of_triangle_is_positive_numbers(arrSidesOfTriangle) == False:
#             flag = False
#         else:
#             flag = True
#     a = int(arrSidesOfTriangle[0])
#     b = int(arrSidesOfTriangle[1])
#     c = int(arrSidesOfTriangle[2])
#     return a, b, c

# проверка и определение типа треугольника
def triangle_check(a, b, c):
    # сравнение длины одной стороны с суммой длин двух других
    if (a < b + c) and (b < c + a) and (c < a + b):
        # является ли треугольник равнобедренным
        if (a == b != c) or (b == c != a) or (c == a != b):
            print('It is isosceles triangle')
        # является ли треугольник равносторонним
        elif (a == b == c):
            print('It is equilateral triangle')
        else:
            # треугольник разносторонний
            print('It is scalene triangle')
    else:
        print('It is not triangle')

# программа №1
# a, b, c = enter_sides_of_triangle_check()
# triangle_check(a, b, c)

# программа №2
print('Enter sides of triangle in format: "A B C". Press the "Enter" key after entering each number')
a, b, c = int(input()), int(input()), int(input())
triangle_check(a, b, c)