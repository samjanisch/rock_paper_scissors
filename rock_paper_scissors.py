import random

def start_game():
    start = ""
    while start  != "y" or "n":
        start = input("Would you like to play rock paper scissors: y/n \n")
        if start == "y":
            play()
        elif start == "n":
            break

def play():
    user = input("'r' for rock, 'p' for paper 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    print("Rock...Paper...Scissors...Shoot")

    print(computer)
    if user == computer:
        return "tie"
    if is_win(user, computer):
        return "You win!"

    return "You Lose!"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'p'):
        return True

def scoreboard():
    user_score = 0

    if_win(user, computer)


print(start_game())

