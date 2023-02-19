# loop until we find 10,001 prime numbers
# check if number is prime
# if it is, increment our count or primes
# if it isn't, continue

def is_prime(n):
    # go through all numbers less than n
    # check if n is divisible by one of those
    # if so, return false
    # if we get to the end, return true
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


print(is_prime(4))
print(is_prime(5))
print(is_prime(9))


found_primes = 0
n = 2

while found_primes <= 10_001:
    if is_prime(n):
        # print(n)
        found_primes += 1
        if found_primes == 10_001:
            print(n)
    n += 1
