# Create a program which searches all the divisors of a number, given by user
# from


numToFactor = int(input("Enter a number:"))

suspect = 2
divisors = [1]
if numToFactor % 2 == 0:
    divisors.append(2)
    numToFactor /= 2
    divisors.append(int(numToFactor))
    multiplier = 2
    while numToFactor % 2 == 0:
        multiplier *= 2
        divisors.append(multiplier)
        numToFactor /= 2
        # divisors.append(int(numToFactor))
suspect = 3
while numToFactor > 1:
    if (numToFactor % suspect == 0):
        divisors.append(suspect)
        numToFactor /= suspect
    else:
        suspect += 2  # only odd
print(divisors)
