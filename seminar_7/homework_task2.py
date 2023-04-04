import os


__all__ = ['bulk_file_renaming']


def raise_serial_number(str_num: str, num_digit) -> str:
    if str_num != '':
        num = int(str_num) + 1
    else:
        num = '1'
    str_num = str(num)
    for _ in range(num_digit-len(str(num))):
        str_num += '0'
    str_num = str_num[::-1]
    return str_num


def bulk_file_renaming(new_name: str, num_digit: int, original_extension: str, new_extension: str, range: list):
    """Method is used for bulk file renaming. It accepts new name for files, number of digits for assignment of \
        a serial numbers, original extension of files, new extension for new files, oriiginal name's range.
        Files must be located in "files_for_rename" dir. Program file and "files_for_rename" dir must be located \
        together.
        For example: bulk_file_renaming('antoshin', 5, '.py', '.txt', [0, 3])
    """
    dir_file_for_rename = os.path.join(os.path.dirname(__file__), 'files_for_rename')
    serial_number = ''
    for roots, dirs, files in os.walk(dir_file_for_rename):
        for file in files:
            if original_extension in file:
                serial_number = raise_serial_number(serial_number, num_digit)
                new_file = file[range[0]:range[1]] + '_' + new_name + '_' + serial_number + new_extension
                os.rename(dir_file_for_rename + '\\' + file, dir_file_for_rename + '\\' + new_file)
