def iter_over_dict(dictionary: dict):
    for k,v in dictionary.items():
        print(f'{k} : {v}')

iter_over_dict({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
