# Создайте функцию генератор чисел Фибоначчи

def gen_fibo(n):
    number_fibo1 = 0
    number_fibo2 = 1
    for i in range(0, n):
        number_fibo_sum = number_fibo1 + number_fibo2
        number_fibo2 = number_fibo1
        number_fibo1 = number_fibo_sum
        i += 1
        yield number_fibo2

n = int(input('Please, enter how much numbers of Fibonacci to display: '))
for i, num in enumerate(gen_fibo(n), start=1):
    if i == n:
        print(num, end='')
    else:
        print(num, end=', ')