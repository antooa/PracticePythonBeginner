# Create a program which searches all the divisors of a number, given by user
# from

import math
#numToFactor = int(input("Enter a number:"))
def search_divisors(numToFactor):
    divisors = list()
    divisors.append(1)
    suspects = range(2, numToFactor + 1)
    for sus in suspects:
        if (numToFactor % sus == 0):
            divisors.append(sus)

    return divisors


