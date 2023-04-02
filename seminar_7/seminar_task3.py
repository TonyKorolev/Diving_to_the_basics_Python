__all__ = ['write_numbers_and_names_to_file']

def write_numbers_and_names_to_file(file1: str, file2: str, file3: str) ->None:
    with (
        open(file1, 'r', encoding='utf-8') as f1,
        open(file2, 'r', encoding='utf-8') as f2,
        open(file3, 'w', encoding='utf-8') as f3
    ):
        # находим кол-во строк в файлах
        lenf1 = sum(1 for _ in f1)
        lenf2 = sum(1 for _ in f2)
        for _ in range(max(lenf1, lenf2)):
            text = f2.readline()
            if text == '':
                f2.seek(0)  # переход в начало файла
                text = f2.readline()
            text = text[: -1]  #убираем последний символ
            num = f1.readline()
            if num == '':
                f1.seek(0)
                num = f1.readline()
            num = num.replace(' ', '')[:-1]  #замена пробелов
            num1, num2 = num.split('|')
            res_mult = int(num1) * float(num2)
            if res_mult < 0:
                f3.write(f'{text.lower()},{abs(res_mult)} \n')
            else:
                f3.write(f'{text.upper()},{round(res_mult)}\n')


if __name__ == '__main__':
    write_numbers_and_names_to_file('numbers.txt','names.txt', 'names_with_numbers.txt')
