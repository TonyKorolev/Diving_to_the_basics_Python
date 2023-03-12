# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

def print_list_with_duplicate_numbers(some_list):
    list_with_duplicate_numbers = []
    distinct_list = []
    for number in some_list:
        if (number in distinct_list):
            list_with_duplicate_numbers.append(number)
        else:
            distinct_list.append(number)
    list_with_duplicate_numbers = list(set(list_with_duplicate_numbers))
    print(list_with_duplicate_numbers)

list_with_numbers = [1, 7, 5, 2, 7, 8, 3, 6, 7, 4, 6, 7, 1, 6, 4, 9]
print_list_with_duplicate_numbers(list_with_numbers)
