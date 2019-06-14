def prime(number):
    if number % 2 ==0:
        is_prime = False
    else:
        is_prime = True
    return is_prime
res = prime(10)
print(res)
