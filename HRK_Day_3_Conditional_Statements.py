
# - Objective

#    In this challenge, we’re getting started with conditional statements.
#    Check out the Tutorial tab for learning materials and an instructional video!

# - Task
#    Given an integer, , perform the following conditional actions:


#    - If N is odd, print Weird
#    - If N is even and in the inclusive range of 2 to 5, print Not Weird
#    - If N is even and in the inclusive range of 6 to 20, print Weird
#    - If N is even and greater than 20, print Not Weird

# - Complete the stub code provided in your editor to print whether or not is weird.

# - Sample Input 0
#    3

# - Sample Output 0
#    Weird

# - Sample Input 1
#    24

# - Sample Output 1
#    Not Weird

'''Need to make it work better'''

N = 18

if not N % 2 == 0:
    print("N is odd")
elif N % 2 == 0 and range(2, 5):
    print("range of 2 to 5")
elif N % 2 == 0 and range(6, 20):
    print("range of 6 to 20")
elif N % 2 == 0 and n > 20:
    print("Abouv 20")


if (N % 2 != 0):
    print("N is odd")
else:
    if (N > 2 and N <= 5):
        print("range of 2 to 5")
    elif (N >= 6 and N <= 20):
        print("range of 6 to 20")
    elif (N >= 20):
        print("Abouv 20 ")
