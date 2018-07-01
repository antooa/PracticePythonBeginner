#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they
#guessed too low, too high, or exactly right.
#Extras:
#  >Keep the game going until the user types “exit”
#  >Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
def main():
    print("Hey, can you guess a number between 1 and 9? Let's figure out!")
    number = random.randint(1, 9)
    guesses = 0
    if_guessed = False
    while not if_guessed:
        guess = input('So try to guess, boy\n')
        if not guess.isnumeric():

            if guess.lower() == 'exit':
                break
            guesses += 1
            print('Only numbers, stupid!')
            continue
        else:
            guess = int(guess)
            guesses += 1

        if guess == number:
            print("Congratulations! The number you chose was {0} and it was correct!" .format(guess))
            if_guessed = True
        elif guess < number:
            print('I regret to tell you that {0} is less than needed!' .format(guess))

        else:
            print('I regret to tell you that {0} is bigger than needed!'.format(guess))

    if if_guessed:
        print("You tried {0} times to guess the number but finally managed to do it!".format(guesses))
    else:
        print("You tried {0} times to guess the number but no soap! :(".format(guesses))

main()