
#   Objective
#
#    - In this challenge, you’ll work with arithmetic operators.
#    - Check out the Tutorial tab for learning materials and an instructional video!
#
#   Task:
#    - Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
#    - and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal’s total cost.
#
#
#    Note:
#   - Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
#
#   - Sample Input
#    12.00
#    20
#    8
#
#   - Sample Output:
#     15

import math
import os
import random
import re
import sys

meal_cost = float(12.0)

tip_percent = int(20)

tax_percent = int(8)

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):

    tip = tip_percent * meal_cost / 100

    tax = tax_percent * meal_cost / 100

    print(round(meal_cost + tip + tax))


solve(meal_cost, tip_percent, tax_percent)

'''So to figure it out we will use the round() function which basically ignores the decimal value and gives a integer output.'''
