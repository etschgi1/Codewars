from collections import Counter
test = "aA11"
test2 = "abcdea"


def duplicate_count(text):
    '''counts duplicate case insensitive input string output int'''
    c = Counter(text.lower())
    return len(([k for k in c if c[k] != 1]))


print(duplicate_count(test))
print("---------")
print(duplicate_count(test2))
