"""Функция словарь, возвращает ключ и значение по номеру введенному пользователем"""

__all__ = ['dict_mystery']


def dict_mystery(num: int) -> list[str]:
    dict_of_mystery: dict[str, str] = {'Два конца, два кольца, посредине гвоздик?': 'ножницы',
                                       'Не огонь, а жжется?': 'крапива',
                                       'Жидкое, а не вода. '
                                       'Белое, а не снег?': 'молоко',
                                       'Без рук, без топорёнка, построена избёнка?': 'гнездо',
                                       'Конь бежит, земля дрожит?': 'гром',
                                       'Летит, а не птица. Воет. а не зверь?': 'ветер',
                                       'Разноцветное коромысло, над рекой повисло?': 'радуга'}

    res = list(dict_of_mystery.items())[num]

    return res


if __name__ == '__main__':
    print(dict_mystery(int(input("Введите номер загадки от 1 до 7: "))))