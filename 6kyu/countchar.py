test = "absiendijcneol"


def count(string):
    dic = {}
    for key in string:
        if key not in dic.keys():
            dic[key] = 1
        else:
            dic[key] += 1
    return dic


def count2(string):
    dic = {}
    for key in string:
        try:
            dic[key] += 1
        except KeyError:
            dic[key] = 1
    return dic


def countonlines(string):
    return {i: string.count(i) for i in string}


print(count2(test))
