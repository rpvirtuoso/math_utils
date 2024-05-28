def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
