#Ask the user for a number and determine whether the number is prime or not.
#(For those who have forgotten, a prime number is a number that has no divisors.).
#You can (and should!) use your answer to Exercise 4 to help you.
#Take this opportunity to practice using functions, described below.
import ListOfDivisors as divs
def check_if_prime(num):
    divisors = divs.search_divisors(num)
    if (divisors[1] == num):
        return True
    else:
        return False
def main():
    num = int(input('Enter the number to check if it\'s prime\n'))
    if check_if_prime(num):
        print('{0} is prime' .format(num))
    else:
        print('{0} is not prime' .format(num))

main()