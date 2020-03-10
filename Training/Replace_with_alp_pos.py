alp = 'abcdefghijklmnopqrstuvwxyz'


def alphabet_position(text):
    seq = ''
    text = text.lower()
    for char in text:
        if char in alp:
            adder = (alp.index(char)+1)
            seq += str(adder) + ' '
    return(str(seq))


print(alphabet_position("DZtJsRidQIIwBcpNGawzOkClazOegPdXpLStJUVsfEfYuFQJCH"
                        "HeaUlfwOaDVuZQMvomktrypXIzvEujUnIqwVXxKUiUqRoXWwmd"))
