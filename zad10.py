def clean_spaces_from_keys(inputDict: dict) -> dict:
        output = {}
        for k,v in inputDict.items():
            new_key = str(k).replace(' ', '')
            output[new_key] = v
        return output

print(clean_spaces_from_keys({' b e j u ': 1, " f r a n ": 2}))   