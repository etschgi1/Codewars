testtext = "This-is_an_example_text."
test2 = "hello-this-second"


def to_camel_case(text):
    '''takes text input with words seperated by underscores or dashes, 
    returns capitalised wordsequenz e.g. hello-world -> helloWorld
    first word is only capital letter in return if in input'''
    # check if dash or underscore for separator
    if '-' in text:
        text = text.replace('-', "_")
    words = list(text.split("_"))
    # add first word to output newwords
    output = ""
    output += words[0]
    # capitalize everything from index 1 on
    for word in words:
        if words.index(word) != 0:
            output += words[words.index(word)].capitalize()
    # return string
    return output


print(to_camel_case(testtext))
