import random

user_name = input("Hello there! What's your name? ")
response = input (f"Do you want to play a game {user_name}? ")

game_start = input(f"I am thinking of a number between 1 and 100. Ready? ")

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = input("Try to guess the number! ")
    guess = int(guess)

    if guess == num:
        print(f"Congratulations {user_name}! You won!")
        break
    elif guess < num:
        print("Your guess is too low, try again!")
    elif guess > num:
        print("Your guess is too high, try again!")
    else:
        print("Nope, sorry. try again!")