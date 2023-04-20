import os

class HomeworkSeminar5():


    def __init__(self, file: str):
        self.file = file


    def __join_elements_list_without_last(self, arr: list) -> str:
        path = ''
        for i in range(len(arr)-1):
            path += arr[i] + '/'
        return path


    def split_relative_path_to_file(self) -> tuple:
        abspath = os.path.abspath(self.file)
        print(abspath)
        path_with_name_file, extension = abspath.split('.')
        list_path_with_name_file = path_with_name_file.split('\\')
        print(list_path_with_name_file)
        name_file = list_path_with_name_file[len(list_path_with_name_file)-1]
        path = self.__join_elements_list_without_last(list_path_with_name_file)
        data = (path, name_file, extension)
        return data
    

s = HomeworkSeminar5('antoshin_file.txt')
# print(s.split_relative_path_to_file())

class Fibo():
    
    
    def __init__(self, n: int):
        self.n = n


    def gen_fibo(self, n: int):
        number_fibo1 = 0
        number_fibo2 = 1
        for i in range(0, n):
            number_fibo_sum = number_fibo1 + number_fibo2
            number_fibo2 = number_fibo1
            number_fibo1 = number_fibo_sum
            i += 1
            yield number_fibo2


    def print_fibonacci_numbers(self):
        for i, num in enumerate(self.gen_fibo(self.n), start=1):
            if i == self.n:
                print(num, end='')
            else:
                print(num, end=', ')

n = int(input('Please, enter how much numbers of Fibonacci to display: '))
f = Fibo(n)
f.print_fibonacci_numbers()