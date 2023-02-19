

a = 1
b = 1
c = 1


def is_pythagorean_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


print(is_pythagorean_triple(3, 4, 5))
print(is_pythagorean_triple(1, 1, 1))

# keep track of a b and c
# keep growing a, and check if the numbers form a triple
# if a is greater than b, increment b, reset a
# similar process for b and c

while not (a + b + c == 1000 and is_pythagorean_triple(a, b, c)):
    if a > b:
        b += 1
        a = 1

    if b > c:
        c += 1
        b = 1

    a += 1

print(a * b * c)
