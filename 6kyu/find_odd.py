from collections import Counter
test = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


def find_it(s):
    '''finds num with odd num of occurences in list'''
    c = Counter(s)
    return ([k for k in c if c[k] % 2 == 1])[0]


print(find_it(test))
