def dropna(dictionary: dict) -> dict:
    to_delete = []
    out = dictionary
    for k,v in out.items():
        if v == None:
            to_delete.append(k)
    for k in to_delete:
        out.pop(k)
    return out

print(dropna({'c1': 'Red', 'c2': 'Green', 'c3': None}))