import random


# def play():
#     user = input("Short name Rock Paper Scissors: R P S:  ")
#     computer = random.choice(['r', 's', 'c'])
#     if computer == user:
#         print("Match is tie ")
#     elif user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
#         print("WOW! User When")
#     else:
#         print("Yey! Computer When")
#     print("Computer Value is: ", computer)
#     print("user Value is: ", user)
#
#
# play()


def play():
    user = input("Short name Rock Paper Scissors: R P S:  ")
    computer = random.choice(['r', 's', 'c'])
    if user == computer:
        return "Match is tie! "
    if win(user, computer):
        return "You Won! "
    print(user)
    print(computer)
    return "You Lose! "


def win(user, computer):
    if user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
        return True


print(play())
