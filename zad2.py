def concat_dict(*args: dict) -> dict:
    out = {}
    for dictionary in args:
        out.update(dictionary)
    return out

dict1 = {1:30, 2:40, 3:50}
dict2 = {4:30, 5:40, 6:50}

print(concat_dict(dict1, dict2))