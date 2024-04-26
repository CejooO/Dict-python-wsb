def count_values(dicitionary: dict, value: any) -> int:
    c = 0
    for v in dicitionary.values():
        if value == v:
            c += 1
            break
    c += 1
    return c

print(count_values({1:2, 2:3, 'fran':4}, 4))
