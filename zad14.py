def sort_list_in_dict(x: dict):
    out = x
    for k,v in out.items():
        if isinstance(v, list):
            out[k] = sorted(v)
    return out

print(sort_list_in_dict({'ent': ['c','b','a'], 'a':'b'}))
