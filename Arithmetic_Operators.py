################
####  Task  ####
################

# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# 1 - The first line contains the sum of the two numbers.
# 2 - The second line contains the difference of the two numbers (first - second).
# 3 - The third line contains the product of the two numbers.


# Example
# a = 3
# b = 5

# Print the following:
# 8
# -2
# 15

# Input Format:
# - The first line contains the first integer, .
# - The second line contains the second integer,

# Output Format:

# - Print the three lines as explained above.

# Sample Input:
a = 6564424525
b = 323252462

# Sample Output:
# - 6887676987
# - 6241172063
# - 2121966389319430550


def summ(a, b):
    return a + b


print(summ(a, b))


def diff(a, b):
    return a - b


print(diff(a, b))


def product(a, b):
    return a * b


# print(product(a, b))

# a = int(input())
# b = int(input())

print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))
