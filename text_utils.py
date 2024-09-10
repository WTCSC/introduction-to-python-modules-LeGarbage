def count_chars(text):
    return len(text) # The len of the text is how many characters it has

def count_words(text):
    return len(text.split()) # Splits the text into words and then counts those

def count_sentences(text):
    return text.count(".") + text.count("?") + text.count("!") # Counts each instance of a ., ?, and !