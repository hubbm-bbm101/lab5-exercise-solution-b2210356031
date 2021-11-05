import random
number = random.randint(1,100)
guessedNumber = int(input("What is your guess?"))
while guessedNumber != number:
    if guessedNumber < number:
        print("Increase your guess!")
        guessedNumber = int(input("Try again: "))
    else:
        print("Decrease your guess!")
        guessedNumber = int(input("Try again: "))
if guessedNumber == number:
    print("You guessed it right!")

