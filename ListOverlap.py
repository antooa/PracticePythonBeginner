# Create a program which prints a list of common elements in two given lists

import random
import sys
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

aSize = int(input("Enter a size of the first list:"))
bSize = int(input("Enter a size of the second list:"))

low = 1  # -sys.maxsize - 1
high = 9  # sys.maxsize

a = [random.randint(low, high) for k in range(aSize)]
b = [random.randint(low, high) for k in range(bSize)]
result = []
for elem in a:
    if elem in b:
        if elem in result:
            continue
        else:
            result.append(elem)
print(result)
