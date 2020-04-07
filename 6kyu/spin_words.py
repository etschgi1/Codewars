test1 = "This is testcase number one"


def spin_words(sentence):
    '''reverses each word with length of 5 or more letters in a sentence
    Input string with one or more words
    Output string with partially reversed or reversed words'''
    spin = ["".join(reversed(w)) if len(
        w) >= 5 else w for w in sentence.split()]
    return " ".join(spin)


print(spin_words(test1))
