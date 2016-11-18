dict1 = {'a': 1, 'c': 3, 'b': 2}
dict2 = {'a': 10, 'e': 30, 'd': 20}

union_of_keys = set(dict1).union(set(dict2))

union_dict = {}
for i in union_of_keys:
    try:
        union_dict[i] = dict1[i]
    except KeyError:
        union_dict[i] = dict2[i]

print union_dict
