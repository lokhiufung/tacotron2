import pinyin

def convert_to_pinyin(text):
    text = pinyin.get(text, format='numerical', delimiter=' ')
    return text

