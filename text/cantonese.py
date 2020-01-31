import jyutping
from .symbols import symbols


def jyutping_handler(char):
    char = jyutping.get(char)[0]
    if type(char) == list:
        char = char[0]
    return char

def convert_to_jyutping(text):
    result = []
    # temp
    text = text.replace('&', 'and')
    text = text.replace('\n', '')
    for char in text.rstrip():
        if char in symbols:
            result.append(char)
        else:
            result.append(jyutping_handler(char))
    return ' '.join(result)
