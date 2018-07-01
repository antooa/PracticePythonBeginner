#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they
#guessed too low, too high, or exactly right.
import random
def main():
    print("Hey, can you guess a number between 1 and 9? Let's figure out!")
    number = random.randint(1, 9)
    guesses = 0
    if_guessed = False
    while not if_guessed:
        guess = input('So try to guess, boy\n')
        if not guess.isnumeric():
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

    print("You tried {0} times to guess the number but finally you managed to do it!" .format(guesses))
main()