test = 456


def helper(n):
    strn = str(n)
    if len(strn) == 1:
        return n
    else:
        return helper(int(strn[1:]))+int(strn[0])


def digital_root(n):
    while len(str(n)) > 1:
        n = helper(n)
    return n


print(digital_root(test))
