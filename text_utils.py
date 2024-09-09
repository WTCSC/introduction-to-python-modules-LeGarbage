def count_chars(text):
    return len(text)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    return text.count(".") + text.count("?") + text.count("!")

print(count_words("Hello, World! How are you?"))
