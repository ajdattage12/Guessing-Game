import random
import math

user_name = input("Hello there! What's your name? ")
print(f"{user_name}, I am thinking of a number between 1 and 100. ")

num = random.randint(1, 100)
guess = None
guessesTaken = 0

while guess != num:
    guess = input("Try to guess the number! ")
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess == num:
        print(f"Congratulations {user_name}! You won in {guessesTaken} guesses!")
        break
    elif guess > 100:
        print("Please pick a number between 1 - 100.")
    elif guess < 1:
        print("Please pick an number between 1 - 100.")
    elif guess < num:
        print("Your guess is too low, try again!")
    elif guess > num:
        print("Your guess is too high, try again!")
    else:
        print("Nope, sorry. try again!")
