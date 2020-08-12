from string import ascii_lowercase, ascii_uppercase
message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = ascii_lowercase
alphau = ascii_uppercase
print(ascii_lowercase)


def rot13(message):
    out = ""
    for l in message:
        ll = l.lower()
        if ll in alpha:
            ind = alpha.index(ll)+13  # get new index
            if ind > 25:
                ind -= 26
            if l.isupper():
                out += alphau[ind]
            else:
                out += alpha[ind]
        else:
            out += l
    return out


print(rot13(message))
