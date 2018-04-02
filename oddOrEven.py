suspect = int(input("Enter the number:"))
parity = ((suspect % 2) == 0)
if parity:
    print(str(suspect) + " is even")
else:
    print(str(suspect) + " is odd")
if (suspect > 2) and (suspect % 4 == 0):
    print(str(suspect) + " is a multiple of 4")
num = int(input("Enter the num :"))
check = int(input("Enter the check:"))
if (num % check == 0):
    print("check divides num evenly")
else:
    print("check doesn't divide num evenly")