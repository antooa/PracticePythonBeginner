# Create a program which checks if a given string is a palindrome(is read the same usually and backwards)

suspectString = input("Enter a string to palindrome check:")
forward = []
backward = []
for char in suspectString:
    forward.append(char)
    backward.insert(0, char)
if forward == backward:
    print(suspectString, "is palindrome")
else:
    print(suspectString, "isn't palindrome")
# a = hash(forward) lists are unhashable
# b = hash(backward)
# print(a - b)
print(forward)
print(backward)
