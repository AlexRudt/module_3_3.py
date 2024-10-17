def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(1, 'egor', False)
print_params(28, 'kirill')
print_params(b = 'kenguru')
print_params(b = 38)
print_params(c = [1, 2, 3])


values_list = [2, 'nice', False]
values_dict = {'a': 36, 'b': 'kow', 'c': True}
print_params(*values_list)
print_params(**values_dict)



values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)