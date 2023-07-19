#Guess the number (Computer guesses)

import random
def computer_guess(x):
    high=x
    low=0
    feedback=""
    while feedback!="c":
        guess=random.randint(low,high)
        print(f"Is your number {guess}?")
        feedback=input("Is your number higher or lower or correct? (h/l/c) ").lower()
        if feedback=="h":
            low=guess+1
        elif feedback=="l":
            high=guess-1
    print(f"Computer guessed your number {guess}!")


x=int(input("What is your range? 0 to "))
computer_guess(x)
