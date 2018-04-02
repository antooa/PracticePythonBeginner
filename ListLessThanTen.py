a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
num = int(input("Enter a number please:"))
userList = []
for element in a:
    if element < 5:
        newList.append(element)
        print(element)
    if element < num:
        userList.append(element)
print(newList)
print("User list:", userList)

