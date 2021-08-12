# Teeny bit of a gotcha. You can create a simple list of all 3 and 5 multiples
# up to some number, but remember that multiples of 15 will be double-counted,
# so either consider that in the initial list creation, or subtract the sum of
# the 15 multiples from the final value.

import sys

LIMIT = 1000


def create_multiples_list_for_x_up_to_y(x, y=LIMIT):
    multiples_list = [x]
    count = 1

    while multiples_list[-1] < y:
        count += 1
        multiples_list.append(x * count)
    multiples_list.pop()  # Don't forget to pop the final element due to the condition having been met, meaning there's one element at the very end that's over the limit

    return multiples_list


def main(limit=LIMIT):
    threes_sum_up_to_limit = sum(create_multiples_list_for_x_up_to_y(3, limit))
    fives_sum_up_to_limit = sum(create_multiples_list_for_x_up_to_y(5, limit))
    fifteens_sum_up_to_limit = sum(create_multiples_list_for_x_up_to_y(15, limit))
    print(
        "Sum of threes: {}; Sum of fives: {}; Sum of fifteens: {}".format(
            threes_sum_up_to_limit, fives_sum_up_to_limit, fifteens_sum_up_to_limit
        )
    )
    print(
        "Sum of multiples of 3 + 5 - 15s (to prevent double-counting): {}".format(
            threes_sum_up_to_limit + fives_sum_up_to_limit - fifteens_sum_up_to_limit
        )
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
