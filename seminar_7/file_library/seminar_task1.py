import random


__all__ = ['generetor_one_int_one_float']


MIN_LIMIT = -1000
MAX_LIMIT = 1000

def generetor_one_int_one_float(count_line:int, file_name:str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count_line):
            tmp_str = str(random.randint(MIN_LIMIT, MAX_LIMIT)) \
            + " | " + str(round(random.uniform(MIN_LIMIT, MAX_LIMIT), 2))
            print(tmp_str)
            f.write(f'{tmp_str}\n')


if __name__ == '__main__':
    count = 5
    generetor_one_int_one_float(count, "numbers.txt")

