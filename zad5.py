def generate_dict(n: int) -> dict:
    output = {}
    for x in range(n):
        output[x] = n*n
    
    return output

print(generate_dict(5))