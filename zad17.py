def combine_lists(keys: list, values: list) -> dict:
    if len(keys) != len(values):
        raise Exception('Length of lists is not the same.')
    for key in keys:
        if keys.count(key) > 1:
            raise Exception('There is more than one occurrence of at least one of the keys in list.')
    out = {}
    for i in range(len(keys)):
        out[keys[i]] = values[i]
    return out

print(combine_lists([1,2,3], ['a','s', 'd']))
