import datetime

name = input("What is your name?")
age = int(input("How old are you?"))
currentYear = datetime.date.today().year
year100 = (currentYear - age) + 100
msg = name + ", you will be 100 years old in " + str(year100)
print(msg)
reps = int(input("How many times do I have to say it so you understand???"))
while reps > 0:
    print(msg)
    reps -= 1
