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

    if player_1_move == rock:
        if player_2_move == scissors:
            return player_1
        elif player_2_move == paper:
            return  player_2
        elif player_2_move == rock:
            return 'draw'
    elif player_1_move == scissors:
        if player_2_move == scissors:
            return 'draw'
        elif player_2_move == paper:
            return  player_1
        elif player_2_move == rock:
            return player_2
    elif player_1_move == paper:
        if player_2_move == scissors:
            return player_2
        elif player_2_move == paper:
            return  'draw'
        elif player_2_move == rock:
            return player_1
def start_game():
    while True:
        print("----------NEW ROUND-----------")
        print(player_1 + "! Now is your turn:")
        player_1_move = input().lower()
        if player_1_move == 'quit':
            break
        print(player_2 + "! Now is your turn:")
        player_2_move = input().lower()
        if player_2_move == 'quit':
            break
        result = play(player_1_move, player_2_move)
        if not result:
            print("FOLLOW THE RULES! ONLY ROCK/SCISSORS/PAPER!")
        elif result == 'draw':
            print(result + '!')
        else:
            print(result + " is winner! CONGRATULATIONS!")


def main():
    print("To quit write \'quit\'")
    print("!!!Game Starts!!!")
    start_game()
    print("Thank you for the game!")

main()