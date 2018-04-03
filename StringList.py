# Create a program which checks if a given string is a palindrome(is read the same usually and backwards)

# import time
suspectString = input("Enter a string to palindrome check:")
forward = str(suspectString)
# The code below checks what is faster: loop reverse or extended slice
# startLoop = time.clock()
# for char in suspectString:
#     forward.append(char)
#     backward.insert(0, char)
# endLoop = time.clock()
# loopTime = endLoop - startLoop
# print(loopTime)
# startRev = time.clock()
backward = suspectString[::-1]
# endRev = time.clock()
# revTime = endRev - startRev
# print(revTime)
# print((revTime > loopTime) - (revTime < loopTime))
# Obviously, extended slice is quicker
# 0.00017918401514446883 - loop
# 2.7356338189995296e-06 - slice
if forward == backward:
    print(suspectString, "is palindrome")
else:
    print(suspectString, "isn't palindrome")
# a = hash(forward) lists are unhashable
# b = hash(backward)
# print(a - b)
print(forward)
print(backward)
