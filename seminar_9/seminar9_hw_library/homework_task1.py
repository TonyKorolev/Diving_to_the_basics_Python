import csv
import random
from typing import Callable
import json

__all__ = ['solve_quadratic_equation', 'gen_abc_in_csv_file']


def _deco_find_answer(func: Callable):
    def wrapper():
        with open('./seminars/seminar_9/num_for_quadratic_equation.csv', 'r', encoding='utf8', newline='') as file:
            file_reader = csv.reader(file, delimiter=';')
            answers = []
            for row in file_reader:
                a, b, c = int(row[0]), int(row[1]), int(row[2])
                x1, x2 = func(a, b, c)[0], func(a, b, c)[1]
                answers.append(f'a = {a}, b = {b}, c = {c}: {x1} {x2}')
        return answers
    return wrapper

def _deco_write_to_json(func: Callable):
    def wrapper():
        answers = func()
        with open('./seminars/seminar_9/answers.json', 'w') as file:
            json.dump(answers, file, indent=2)
    return wrapper

@_deco_write_to_json
@_deco_find_answer
def solve_quadratic_equation(a: int, b: int, c: int) -> list:
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = round((-b + D**(1/2)) / 2 / a, 2)
        x2 = round((-b - D**(1/2)) / 2 / a, 2)
    elif D == 0:
        x1 = x2 = round((-b + D**(1/2)) / 2 / a, 2)
    else:
        x1 = 'No roots'
        x2 = ''
    return [x1, x2]

def _get_random_num() -> int:
    num = 0
    while num == 0:
        num = random.randint(-100, 100)
    return num

def gen_abc_in_csv_file():
    with open('./seminars/seminar_9/num_for_quadratic_equation.csv', 'w', encoding='utf8', newline='') as file:
        file_writer = csv.writer(file, dialect='excel', delimiter=';',\
                                    quoting=csv.QUOTE_MINIMAL)
        for _ in range(100):
            file_writer.writerow([_get_random_num() for _ in range(3)])

gen_abc_in_csv_file()
solve_quadratic_equation()