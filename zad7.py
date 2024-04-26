d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

def counter(x:dict, y:dict):
    output = x
    for k,v in y.items():
        if k in output.keys():
            output[k] += v
        else:
            output[k] = v
    return output
print(counter(d1, d2))
