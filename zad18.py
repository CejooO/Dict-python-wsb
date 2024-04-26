def get_max_and_min_key(x:dict):
    matchers = [min(x.values()), max(x.values())]
    out = []
    for k,v in x.items():
        if v in matchers:
            out.append(k)
    return out

print(get_max_and_min_key({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))
