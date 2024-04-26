def is_empty(x: dict) -> bool:
    return str(x.keys()) == 'dict_keys([])'

print(is_empty({1:2}))