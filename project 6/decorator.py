def red(f):
    def inner(*args):
        out = "\033[31;7m" + f(*args) + "\033[0m"
        return out

    return inner


def blue(f):
    def inner(*args):
        out = "\033[34;1m" + f(*args) + "\033[0m"
        return out

    return inner


def red_underline(f):
    def inner(*args):
        out = "\033[31;4m" + f(*args) + "\033[0m"
        return out

    return inner


@red
@red_underline  # words = red(words)
def words(text):
    return text


print(words("hello"))
