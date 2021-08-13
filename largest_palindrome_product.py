# Added fluff to this one, in that you can provide an arbitrary product limit to the function:
#
# Example:
# ➜  project_euler_scripts git:(main) ✗ py3 largest_palindrome_product.py 2 2000
# Found a palindrome product for 2 digit factors: (99 * 91 = ) 9009
# The product was larger than the limit 2000, so skipping!
# Found a palindrome product for 2 digit factors: (97 * 55 = ) 5335
# The product was larger than the limit 2000, so skipping!
#
# ...
#
# Found a palindrome product for 2 digit factors: (57 * 33 = ) 1881
# Found a palindrome product for 2 digit factors: (53 * 44 = ) 2332
# The product was larger than the limit 2000, so skipping!
# Found a palindrome product for 2 digit factors: (48 * 44 = ) 2112
# The product was larger than the limit 2000, so skipping!
# The largest palindrome product for 2 digit factors is 1881

import sys

DIGITS_FOR_PRODUCT_PALINDROME_CHECK = 2


def number_palindrome_checker(num):
    """Uses Python's slice indices feature to help check for palindrome-ness

    Introduced in Python-1.4 (at numpy's behest no less!) https://docs.python.org/3/whatsnew/2.3.html?highlight=slice#extended-slices

    The "[::-1]" slice indices syntax can reverse lists, and is used here with the string representation of the number

    Example with plain strings:
        >>> "careful"[::-1]
        'luferac'
    """
    return str(num) == str(num)[::-1]


def main(digits=DIGITS_FOR_PRODUCT_PALINDROME_CHECK, product_limit=False):
    # First things first, we want to ensure we check for LARGE products, so start at
    # the far end, with 10 ^ digits - 1 as the top value, and one below that for the 2nd

    # E.g.: 999 and 998 for limits of 3 digits
    largest_factor = pow(10, digits) - 1
    second_largest_factor = largest_factor - 1
    product = largest_factor * second_largest_factor

    # Keep a record of the lowest product when we hit a palindrome product, since any
    # competing factors should have a higher secondary factor than what we saw before.
    #
    # E.g.: If 999 * 50 is a palindrome, we'd never want to check 998 * 50 or below, since
    # our first number will be lowering as well, and there's no point in checking smaller
    # factors.
    lowest_factor_limit = 0

    # We need to keep a running count of the palindromes we see, in case a later value is
    # larger than the first one we see.
    #
    # E.g.:
    # ➜  project_euler_scripts git:(main) ✗ py3 largest_palindrome_product.py 3
    # Found a palindrome for 3 digit factors: (995 * 583 = ) 580085
    # Found a palindrome for 3 digit factors: (993 * 913 = ) 906609
    # Found a palindrome for 3 digit factors: (968 * 916 = ) 886688
    # Found a palindrome for 3 digit factors: (962 * 924 = ) 888888
    # The largest palindrome product for 3 digit factors is 906609
    big_product_palindrome_list = []

    # Defaults the product_limit to either the passed-in value, or a number larger than
    # any calculated product based on our digits
    if product_limit:
        product_limit = min(product_limit, pow(10, digits * 2))
    else:
        product_limit = pow(10, digits * 2)

    # Check two conditions:
    # 1. The large factor should never go beyond the lowest factor we've had that matched a valid palindrome product
    # 2. The large factor should always have X digits
    while largest_factor > lowest_factor_limit and largest_factor > (
        pow(10, digits - 1) - 1
    ):
        # Check the same two conditions as the large factor!
        while second_largest_factor > lowest_factor_limit and second_largest_factor > (
            pow(10, digits - 1) - 1
        ):
            if number_palindrome_checker(product):
                print(
                    "Found a palindrome product for {} digit factors: ({} * {} = ) {}".format(
                        digits, largest_factor, second_largest_factor, product
                    )
                )
                # If we have a product_limit that restricts us, skip the following logic and continue our search
                if product > product_limit:
                    print(
                        "The product was larger than the limit {}, so skipping!".format(
                            product_limit
                        )
                    )
                    break
                # Once we've found a match, increase our lower limit to the smaller factor, then append the match to our list
                lowest_factor_limit = second_largest_factor
                big_product_palindrome_list.append(product)
            # Go through each number, counting down the smaller factor and also reducing the product
            second_largest_factor -= 1
            product -= largest_factor
        # Exhausted options available for the larger factor, so reduce the large factor by one and reset
        # the smaller factor and the calculated product
        largest_factor -= 1
        second_largest_factor = largest_factor - 1
        product = largest_factor * second_largest_factor

    if not big_product_palindrome_list:
        print(
            "No palindrome product was found that met the requirements of having {} digit factors "
            "AND being under the limit of {}.".format(digits, product_limit)
        )
        return

    print(
        "The largest palindrome product for {} digit factors is {}".format(
            digits, max(big_product_palindrome_list)
        )
    )


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
