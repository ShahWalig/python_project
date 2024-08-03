import random

random_number = random.randint(1, 10)
user = 1000
while user != random_number:
    user = int(input("Enter your guess for the computer's number (1 T0 10) : "))

    if user == random_number:
        print("You guessed the correct number!")

    elif user > random_number:
        print("Your number is greater than the computer's guessed number.")
    else:
        print("Your number is less than the computer's guessed number.")

#use Function same code 
#import random
# 
# 
# def guess(x):
#     random_number = random.randint(1, x)
#     guess_user = 1000
#     while guess_user != random_number:
#         guess_user = int(input("Enter your guess for the computer's number (1 T0 10) :"))
#         if guess_user < random_number:
#             print("Your Number is Less then .")
#         elif guess_user > random_number:
#             print("Your Number is Greater then .")
# 
#     print("WOO YAA: Congregate Your number is less than the computer's guessed number.")
# 
# 
# guess(10)
