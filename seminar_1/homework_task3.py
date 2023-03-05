# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч

# проверяем простоту
def is_prime(num):
    if num == 0:
        print('0 is not prime number')
    elif num == 1:
        print('1 is prime number')
    else:
        NumIsPrime = True
        for i in range(2, (num//2)+1):
            if num % i == 0:
                NumIsPrime = False
                break
        if NumIsPrime == False:
            print(f'{num} is composite number')
        else:
            print(f'{num} is prime number')

# просим ввести корректные данные
def enter_number_check(max_num):
    num = -1
    while (num < 0 or num > max_num):
        num = int(input(f"Enter number from 0 to {max_num}:\n"))
    return num

# программа
number = enter_number_check(max_num=100000)
is_prime(number)
    