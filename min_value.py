#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program generate 10 random numbers
# and returns the min value

import random

# Defining the function that returns the min value using for...each loop
def min_value(list):
    min_val = 101
    for a_num in list:
        if a_num < min_val:
            min_val = a_num
    return min_val


def main():
    # Creating empty list and "max_num" variable
    nums = []
    min_num = 0
    # Generating the 10 random numbers
    for counter in range(10):
        random_num = random.randint(0, 100)
        nums.append(random_num)
        print("{} added to list at index {}".format(random_num, counter))

    # Calling the function
    min_num = min_value(nums)

    # Displaying the min number
    print()
    print("The min number is {}".format(min_num))


if __name__ == "__main__":
    main()
