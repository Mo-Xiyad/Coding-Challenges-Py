################
####  Task  ####
# ################
#
#  - The included code stub will read an integer, N , from STDIN.
#
#  - Without using any string methods, try to print the following:
#
#  - 123...N
#
#  - Note that "..." represents the consecutive values in between.
#
#  -Example
#
#     N = 5
#
#  - Print the 1 2 3 4 5 string .
#
#   - Input Format
#
#     The first line contains an integer N.
#
#  - Output Format
#
#  - Print the list of integers from  through  as a string, without spaces.

# - Sample Input 0

n = 3

# - Sample Output 0
#   1 2 3

i = 1
while i <= n:
    print(i, end="")
    i = i+1
