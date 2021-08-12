# Example usage: (the last number printed is the GCF for the entire list of numbers)
# ➜  project_euler_scripts git:(main) ✗ py3 gcf_euclid.py 182664,154875,137688
# [182664, 154875, 137688]
# 177
# 3

import sys


def _euclid(x, y):
    """Implement Euclid's algorithm: https://www.calculatorsoup.com/calculators/math/gcf.php#euclid

    1. Given two whole numbers, subtract the smaller number from the larger number and note the result.
    2. Repeat the process subtracting the smaller number from the result until the result is smaller than the original small number.
    3. Use the original small number as the new larger number. Subtract the result from Step 2 from the new larger number.
    4. Repeat the process for every new larger number and smaller number until you reach zero.
    5. When you reach zero, go back one calculation: the GCF is the number you found just before the zero result.
    """
    small = min(x, y)
    big = max(x, y)
    diff = 1  # Canned GCF is 1
    if x <= 0 or y <= 0:
        raise RuntimeError("One of the numbers is 0 or negative! Not allowed!")

    # Ex: 3 , 2
    while (
        big - small != 0
    ):  # If we reach zero, return the diff before the big - small calculation
        diff = big - small  # 1. 1 = 3 - 2; 2. 1 = 2 - 1; 3. 0 = 1 - 1
        while True:
            if diff <= small:  # 1 < 2
                big = small  # big = 2
                small = diff  # small = 1
                break
            diff = diff - small

    return diff


def main(arr):
    """Define some triplets and recover the only valid string they could combine into"""
    gcf = arr[0]
    for i in range(len(arr) - 1):
        gcf = _euclid(gcf, arr[i + 1])
        print(gcf)
    return gcf


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(list(map(int, sys.argv[1].strip("[]").split(","))))
        main(list(map(int, sys.argv[1].strip("[]").split(","))))
