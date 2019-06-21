def is_triangle(a, b, c):
    if a<b+c and b<a+c and c<a+b:
        return True

    return False


print(is_triangle(5, 2, 5))