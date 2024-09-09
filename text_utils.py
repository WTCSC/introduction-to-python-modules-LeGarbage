def count_chars(text):
    return len(text)

def count_words(text):
    return text.count(" ")

def count_sentences(text):
    return text.count(".") + text.count("?") + text.count("!")
