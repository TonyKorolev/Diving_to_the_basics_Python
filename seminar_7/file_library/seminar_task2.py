import random


__all__ = ['create_name']


vowels_letters = "аеиоуыэюя"
consonants_letters = "бвгджзйклмнпрстфхцчшщъь"

def create_name(count_line:int, file_name:str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count_line):
            result_str = ""
            for _ in range(random.randint(4, 7)):
                num = random.randint(0, 1)
                if num == 0:
                    result_str += random.choice(vowels_letters)
                else:
                    result_str += random.choice(consonants_letters)
            result_str = result_str.capitalize()
            print(result_str)
            f.write(f'{result_str}\n')


if __name__ == '__main__':
    count = 6
    create_name(count, 'names.txt')
