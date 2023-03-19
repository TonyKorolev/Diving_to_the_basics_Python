# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def join_elements_list_without_last(arr: list) -> str:
    path = ''
    for i in range(len(arr)-1):
        path += arr[i] + '/'
    return path

def split_relative_path_to_file(file: str) -> tuple:
    abspath = os.path.abspath(file)
    print(abspath)
    path_with_name_file, extension = abspath.split('.')
    list_path_with_name_file = path_with_name_file.split('\\')
    print(list_path_with_name_file)
    name_file = list_path_with_name_file[len(list_path_with_name_file)-1]
    path = join_elements_list_without_last(list_path_with_name_file)
    data = (path, name_file, extension)
    return data


print(split_relative_path_to_file('antoshin_file.txt'))