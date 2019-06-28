def is_prime2(num):
    is_prime = True
    i = 2

    while i < num:
        if num % i == 0:
            is_prime = False
        i += 1
    return is_prime, print(is_prime)


def prime_number():
    num = 1
    while True:
        num += 1
        if is_prime2(num):
            yield num


gen = prime_number()
for i in gen:
    print(i)
