#! A simple gave Rock Paper Scissors
print('Welcome to the game Rock Scissors Paper!\nI hope you know the rules :D')
player_1 = input('FIRST player, what is your name?\n')
player_2 = input('SECOND player, what is your name?\n')

rock = 'rock'
scissors = 'scissors'
paper = 'paper'

def play(player_1_move, player_2_move):
    if player_1_move != rock and player_1_move != scissors and player_1_move != paper:
        return False
    if player_2_move != rock and player_2_move != scissors and player_2_move != paper:
        return False
    if player_2_move == player_1_move:
        return 'Its a draw'
    else:
        if player_1_move == rock:
            if player_2_move == scissors:
                return player_1
            elif player_2_move == paper:
                return player_2
        elif player_1_move == scissors:
            if player_2_move == paper:
                return player_1
            else:
                return player_2
        elif player_1_move == paper:
            if player_2_move == scissors:
                return player_2
            else:
                return player_1

def start_game():
    while True:
        print("----------NEW ROUND-----------")
        print("{0}! Now is your turn:" .format(player_1))
        player_1_move = input()

        if player_1_move == 'quit':
            break
        print("{0}! Now is your turn:" .format(player_2))
        player_2_move = input()

        if player_2_move == 'quit':
            break
        result = play(player_1_move.lower(), player_2_move.lower())
        if not result:
            print("FOLLOW THE RULES! ONLY ROCK/SCISSORS/PAPER!")
        elif result == 'draw':
            print('{0}!' .format(result))
        else:
            print("{0} is winner! CONGRATULATIONS!" .format(result))


def main():
    print("To quit write \'quit\'")
    print("!!!Game Starts!!!")
    start_game()
    print("Thank you for the game!")

main()