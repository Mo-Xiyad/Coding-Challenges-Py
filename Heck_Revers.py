#!/bin/python3

import math
import os
import random
import re
import sys


def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split()
# reversing the words using reversed() function
    words = list(reversed(words))
# joining the words and printing
    j = " ".join(words)
    return j.swapcase()


print(reverse_words_order_and_swap_cases("aWESOME is cODING"))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    # fptr.write(result + '\n')

    # fptr.close()
