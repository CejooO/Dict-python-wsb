def does_key_exist(key: any, dictionary: dict) -> bool:
    return key in dictionary.keys()

print(does_key_exist('bu',{'beju': 1, 'fran': 2}))