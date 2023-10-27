import random

print("Rock, paper, Scissors! enter your choice:")
def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'its a tie'
    
    if is_win(user, computer):
        return "you win!"
    
    return "you lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent =='r') :
        return True

def main():
    while 1 == 1 : 
        print(play())

main()
    