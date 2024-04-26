def create_string_dict(variable: str) -> dict:
    out = {}
    for x in range(len(variable)):
        out[x + 1] = variable[x]
    return out

print(create_string_dict('w3resource'))