def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [10, 'String', True]
values_dict = {'a': True, 'b': 13, 'c': 'String'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [False,'String']
print_params(*values_list_2, 42)