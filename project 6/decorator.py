def red(f):
    def inner(*args):
        out = "\033[31;1m" + f(*args) + "\033[0m"
        return out

    return inner


def blue(f):
    def inner(*args):
        out = "\033[34;1m" + f(*args) + "\033[0m"
        return out

    return inner


@red  # words = red(words)
def words(text):
    return text


print(words("hello"))
