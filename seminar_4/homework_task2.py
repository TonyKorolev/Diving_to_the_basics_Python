# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ - значение переданного аргумента, а значение - имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def print_kwargs_dict(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, list) or isinstance(value, set) or isinstance(value, tuple):
            kwargs.update(dict([(key, str(value))]))
    dictionary = dict(zip(kwargs.values(), kwargs.keys()))
    print(dictionary)

print_kwargs_dict(a=5, b=7.0, name='Tony', flag=True, arr=[1, 3, 5], even={2, 4, 6}, bin_nums=(0, 1))

