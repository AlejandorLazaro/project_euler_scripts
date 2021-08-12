# Mostly transcribed from https://www.geeksforgeeks.org/find-largest-prime-factor-number/,
# I still don't like the fact that this seems like a wierdly magic solution with little
# explanation of why we start real prime searches after 2 and 3 with 5 and jump ahead with
# intervals of 6 (+2) after that...

import sys


def prime_fact(n):
    max_prime = -1
    while not n % 2:
        max_prime = 2
        n >>= 1
    while not n % 3:
        max_prime = 3
        n = int(n / 3)
    i = 5
    ROOT = int(pow(n, 1 / 2))
    while i <= ROOT:
        while not n % i:
            max_prime = i
            n = int(n / i)
        while not n % (i + 2):
            max_prime = i + 2
            n = int(n / (i + 2))
        i += 6
    if n > 4:
        max_prime = n
    return max_prime


def main(num_to_find_largest_factor_for=100):
    print(prime_fact(num_to_find_largest_factor_for))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
