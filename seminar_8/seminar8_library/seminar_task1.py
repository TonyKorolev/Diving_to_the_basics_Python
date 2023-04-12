import json

__all__ = ['convert_to_json']

def convert_to_json(file_name: str) -> None:
    dictionary = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            arr = line.split(',')
            dictionary[arr[0].capitalize()] = float(arr[1])
    with open('./seminars/seminar_8/file_json.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

convert_to_json('./seminars/seminar_8/names_with_numbers.txt')
