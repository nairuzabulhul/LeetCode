#!/usr/bin/python
# -*- coding: utf-8 -*-


def insert_position(number, arr):

    if len(arr) == 0:

        return None

    # loop through the array

    for i in arr:

    # compare number to the array numbers

        if number in arr:

    # if found , return the index

            return arr.index(number)
        else:

            if number < i:

                sub = []

                for n in arr:

                    if number < n:

                        sub.append(n)

                min_num = min(sub)

                return arr.index(min_num)
            elif number > i:

                sub = []

                for n in arr:

                    if number > n:

                        sub.append(n)

                max_sub = max(sub)

                return arr.index(max_sub) + 1


# Output 
arr = [1, 3, 5, 6]
number = 7
print insert_position(number, arr)

            
