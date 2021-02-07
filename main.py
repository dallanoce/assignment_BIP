#!/usr/bin/env python3


def maxSubArray(lst):
    """
    The function receives an array of integers as input and returns the sub-array that has the largest sum.

    :param lst: input list of integers
    :return: maximum sum, corresponding subarray
    """

    max_current = lst[0]
    result_sub = []

    current_sum = 0
    current_sub = []

    for x in lst:

        if x >= 0:
            current_sum += x
            current_sub.append(x)
            if current_sum >= max_current:
                result_sub = current_sub.copy()
                max_current = current_sum

        else:
            if current_sum + x < 0:

                current_sum = 0
                current_sub = []
            else:
                current_sum += x
                current_sub.append(x)

            if max_current <= 0 and x >= max_current:  # to handle the case where there are only negative values
                # in the array
                max_current = x
                result_sub = [x]

    return max_current, result_sub


def main():
    """
    input example:
    3

    -6
    2
    3
    """
    # creating an empty list
    lst = []

    # number of elements as input
    n = int(input())
    input()  # empty line

    # iterating until the range
    for i in range(0, n):
        el = int(input())
        lst.append(el)  # adding the element

    print(lst)

    max_sum, subarray = maxSubArray(lst)  # function required

    print("max sum: " + str(max_sum))
    print("corresponding subarray: " + str(subarray))


if __name__ == "__main__":
    main()
