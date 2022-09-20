import random

number = random.randint(1,20)

guess = int(input("I'm thinking of a number between 1 and 20. What is it? "))

while guess != number:
    if guess < number:
        print("Your guess was too low...")
    else:
        print("Your guess was too high...")
    guess = int(input("Guess again... "))
print("You guessed the number!")