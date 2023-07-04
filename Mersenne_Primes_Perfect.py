# Checks if a number n is a prime number.
def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

# Checks is 2^n - 1 is a Prime Number.
def is_mersenne_prime(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    if is_prime(2**n - 1):
        return 1
    return 0

# Returns the Perfect up until Mersenne Index n
def perfect_numbers(n):
    d = {}
    for i in range(2, n + 1):
        if is_mersenne_prime(i):
            d[i] = (2**(i - 1)) * (2**i - 1)
    return d