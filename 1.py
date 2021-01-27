def my_format(string, char = '!'):
    result_string = f'{char}{string}{char}'
    return result_string

print(my_format(5))