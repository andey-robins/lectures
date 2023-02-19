def is_multiple_three(n):
    if n % 3 == 0:
        return True
    else:
        return False


def is_multiple_five(n):
    if n % 5 == 0:
        return True
    else:
        return False


def is_multiple_three_or_five(n):
    return is_multiple_three(n) or is_multiple_five(n)


n = 1
multiples_sum = 0

while n < 10_000_000:
    if is_multiple_three_or_five(n):
        multiples_sum += n
    n += 1

print(multiples_sum)
