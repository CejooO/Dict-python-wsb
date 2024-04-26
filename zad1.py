def add_key(dictionary:dict, key):
    dictionary[key] = None
    return dictionary

dtest = {1:0,
         2:10,
         3:20}
print(dtest)
print(add_key(dtest, 5))