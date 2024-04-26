def remove_duplicates(x:dict) -> dict:
    out = {}
    for k,v in x.items():
        if k not in out.keys():
            out[k] = v
    return out

print(remove_duplicates({1:2, 2:3, 2:3}))