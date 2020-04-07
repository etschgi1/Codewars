word = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada']


def anagrams(word, words):
    sword = "".join(sorted(word))
    out = []
    for w in words:
        sw = "".join(sorted(w))
        if sw == sword:
            out.append(w)
    return out


print(anagrams(word, words))
