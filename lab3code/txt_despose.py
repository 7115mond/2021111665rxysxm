def replace_punctuation_with_whitespace(text):
    punctuation = [',', '.', '?', '!', ':', ';', '-', '(', ')', '[', ']', '{', '}', "'", '"','@','   ','  ','    ']
    for char in punctuation:
        text = text.replace(char, ' ')
    text = text.lower()
    text = text.replace('\n', '').replace('\r', '')
    return text


