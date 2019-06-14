def word_split(text, ignore=False):
    if ignore == True:
        text.lower()
    words = text.split()
    return set(words)


word_split("hello darkness my my old friend")

