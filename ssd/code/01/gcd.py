#!/usr/bin/python3

def main():

    print("Calculating the greatest divisor of 2^18")
    n = 2 ** 18

    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            print(f'The greatest divisor is {int(n / i)}')
            print(f'{n} / {int(n/i)} = {i}')
            return

if __name__ == "__main__":
    main()