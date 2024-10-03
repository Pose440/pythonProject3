data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*args):
    num = 0
    for item in args:
        if isinstance(item,int):
            num += item
        elif isinstance(item,str) and len(item) > 0:
            num += len(item)
        elif isinstance(item, (tuple, set, list)):
            num += calculate_structure_sum(*item)
        elif isinstance(item,dict):
            num += calculate_structure_sum(*item.keys())
            num += calculate_structure_sum(*item.values())
    return num



result = calculate_structure_sum(data_structure)
print(result)



