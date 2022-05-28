import random
import time

def play():
    user = input("Select 'r' for rock, or 'p' for paper, or 's' for scissors\n"
                 ">>> ")
    print(f'You selected "{user}"')
    computer = random.choice(['r', 'p', 's'])
    print('Wait for computer to select...')
    time.sleep(0.5)
    print(f'Computer selected "{computer}"')
    # rule: r > s, s > p, p > r
    time.sleep(0.5)
    if user == computer:
        return 'Its a tie..'

    if is_win(user, computer):
        return 'You won..'
    return 'You lost..'


def is_win(player, opponent):
    # returns if player wins
    # rule: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())