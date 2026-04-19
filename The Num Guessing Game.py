import random

"""lowest_num = 1 #comment
highest_num = 100
"""
toStoreRndmGuessedNum = random.randint(1,100)
# print(toStoreRndmGuessedNum)
attempts = 0
is_running = True
print("---Welcome to The Guessing Game---")
print("Guess a Number between 1 to 100")
while is_running:
    try:

        guess= int(input("Enter your Guessed Number: "))
        attempts +=1
        
        if guess > toStoreRndmGuessedNum:
            print("Guessed Number is to High")
        elif guess < toStoreRndmGuessedNum:
            print("Guessed Number is to Low")

        else:
            print(f"Congratulations..! You Guessed correct Number {guess} in {attempts} Attempts.")
            is_running = False

    except ValueError:
        print("Enter a Vaid Whole Number")