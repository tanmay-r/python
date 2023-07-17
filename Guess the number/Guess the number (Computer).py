#Guess the number (Computer)
import random

def guess(n):
   random_number=random.randint(1,n)
   u_guess=0

   while u_guess!=random_number:
    u_guess=int(input("Guess a number: "))
       
    if u_guess>random_number:
        print("You guessed too high!")
    elif u_guess<random_number:
        print("You guessed too low!")
        
   print("You have guessed the number!")
    
    

    
n=int(input("Enter a range: 1 to "))
guess(n)
