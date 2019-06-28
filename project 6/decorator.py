def red(f):
    def inner(*args):
        out = "\033[31;1m" + f(*args) + "\033[0m"
        return out

    return inner


@red
def words(text):
    return text


# words = red(words)
print(words("hello"))
