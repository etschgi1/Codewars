test = [{'name': 'test'}]
namesin = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
name = []


def namelist(names):
    # for empty dict
    if not names:
        return ''
    for e in names:
        name.append(e["name"])
    # for single item in list
    if len(name) == 1:
        return name[0]
    # for multiple items
    return ", ".join(name[0: -1])+" & "+name[-1]


print(namelist(namesin))
