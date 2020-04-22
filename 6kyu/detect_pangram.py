import string
test = "The quick brown fox jumps over the lazy dog!!!!"


def is_pangram(s):
    s = s = "".join([i for i in s if i.isalpha()])
    if len("".join(set(s))) > 25:
        return True
    return False


print(is_pangram(test))
print(string)
