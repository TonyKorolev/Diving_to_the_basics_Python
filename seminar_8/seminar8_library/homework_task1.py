import os
import json
import csv
import pickle

__all__ = ['get_all_dirs_and_files']

def _get_size_files_in_dir(path_to_dir: str) -> str:
    sum_size = 0
    for roots, dirs, files in os.walk(path_to_dir):
        for file in files:
            sum_size += file.__sizeof__()
    return sum_size

def get_all_dirs_and_files(name_dir: str) -> tuple:
    dictionary_dirs_and_files = {}
    for roots, dirs, files in os.walk(name_dir):
        for dir in dirs:
            dictionary_dirs_and_files[dir] = [os.path.join(name_dir), 'dir', _get_size_files_in_dir(os.path.join(name_dir, dir))]
        for file in files:
            dictionary_dirs_and_files[file] = [os.path.join(name_dir), 'file', _get_size_files_in_dir(os.path.join(name_dir, dir))]
    
    with open('dirs_and_files.json', 'w') as f:
        json.dump(dictionary_dirs_and_files, f, indent=4)

    with open('dirs_and_files.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['Object', 'ParentPath', 'Type', 'Size'], dialect='excel', delimiter=' ',\
                                    quoting=csv.QUOTE_MINIMAL)
        csv_writer.writeheader()
        dict_row = {}
        for key, value in dictionary_dirs_and_files.items():
            dict_row['Object'] = key
            dict_row['ParentPath'] = value[0]
            dict_row['Type'] = value[1]
            dict_row['Size'] = value[2]
            csv_writer.writerow(dict_row)

    with open('dirs_and_files.pickle', 'wb') as f:
        pickle.dump(dictionary_dirs_and_files, f)

get_all_dirs_and_files(r'G:\GeekBrains\Diving to the basics Python\seminars\seminar_8\test_dir')