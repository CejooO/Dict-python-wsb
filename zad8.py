def generate() -> dict:
    out = {}
    for n in range(1,16):
        out[n] = n*n
    return out

print(generate())