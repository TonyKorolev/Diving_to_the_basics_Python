# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант

import random

def print_things_list(dictionary: dict):
    things_list = []
    weight = 0
    dict_copy = dictionary.copy()
    while dict_copy:
        random_thing = random.choice(list(dict_copy.keys()))
        if weight + dict_copy.get(random_thing) < max_load_capacity_backpack:
            things_list.append(random_thing)
            weight += dict_copy.get(random_thing)
            dict_copy.pop(random_thing)
        else:
            dict_copy.pop(random_thing)
            continue
    print(things_list, f'\nМасса рюкзака {weight/1000} кг')

things_and_weight_dict_for_trip = {'трико': 200, 'кофта': 300, 'термобелье': 300, 'футболка': 100, 'нижнее белье': 200,\
                                   'спальный мешок': 1800, 'дождевик': 400, 'коврик': 800, 'кружка': 100, 'термос': 2000, \
                                    'фонарик': 600, 'аптечка': 1200, 'средства личной гигиены': 1000, 'ложка': 100,\
                                    'палатка': 2200, 'куртка': 800, 'чашка': 100, 'навигатор': 200, 'вода': 2000, 'ножи': 200,\
                                    'обувь': 800, 'спички': 50, 'горелка': 500}

max_load_capacity_backpack = int(input('Введите максимальную грузоподъемность рюкзака в килограммах:\n'))*1000
print_things_list(things_and_weight_dict_for_trip)

