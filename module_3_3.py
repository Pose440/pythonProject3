def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c,)

print_params(1,"строка", True)
print_params()
print_params(b = 25)
c = [1, 2, 3]
print_params(c = [1, 2, 3])

values_list = [3, "pops", True]
values_dict = {"a" : 45, "b" : "rocket", "c" : False }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [23, "Fedya"]
print_params(*values_list_2, 42 )

