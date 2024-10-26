from inspect import getmembers, isfunction
import functions


def get_list_of_functions():
    list_of_functions = []

    get_functions = getmembers(functions, isfunction)
    for item in get_functions:
        list_of_functions.append(item[0])

    return ', '.join(map(str, list_of_functions))

