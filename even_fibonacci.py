# Easy fibonacci creation, with just a requirement to understand lists and filters
#
# Example usage:
# ➜  project_euler_scripts git:(main) ✗ py3 even_fibonacci.py 672349241340
# 478361013020

import sys

LIMIT = 10000


def fibonacci_sequence_generator(limit=LIMIT):
    fibonacci_seq = [1, 2]

    while fibonacci_seq[-1] < limit:
        fibonacci_seq.append(fibonacci_seq[-2] + fibonacci_seq[-1])
    fibonacci_seq.pop()  # Don't forget to pop the final element due to the condition having been met, meaning there's one element at the very end that's over the limit

    return fibonacci_seq


def main(limit=LIMIT):
    print(sum(list(filter(lambda x: not x % 2, fibonacci_sequence_generator(limit)))))
    # The magic here is the use Python's filter function, which allows us to run a function
    # (of which lambda is a temporary function) on all elements of an iterable (say, a list),
    # and only return values that the function returns truthy.
    #
    # In this case, only even numbers return 0 for modulo 2, and inverting the result will filter
    # out all even numbers, which I can then sum together.
    #
    # Note: You must use an encapsulating 'list' call in Python3, as 'map', 'filter', and more now
    # return specialized iterator objects for each function instead of the lists as in Python2.7

    # Example:
    #
    # Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52)
    # >>> foo = [1]
    # >>> filter(lambda x: x, foo)
    # <filter object at 0x7fbd9a578ca0>
    # >>> map(lambda x: x, foo)
    # <map object at 0x7fbd9a655b80>
    #
    # Python 2.7.16 (default, May  8 2021, 11:48:02)
    # >>> foo = [1]
    # >>> filter(lambda x: x, foo)
    # [1]
    # >>> map(lambda x: x, foo)
    # [1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
