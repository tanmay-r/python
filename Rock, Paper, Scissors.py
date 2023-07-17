
#rock paper scissors that goes on infinitely and keeps score.
import random
p_score=0
c_score=0

while True:
    
    
    player_choice=input("Enter you choice (rock, paper or scissors):").lower()
    choices=["rock", "paper", "scissors"]
    computer_choice=random.choice(choices)

    if player_choice!=computer_choice:
        print("Your choice:", player_choice)
        print("Computer choice:", computer_choice)

        if computer_choice=="rock":
            if player_choice=="scissors":
                print("Computer wins!")
                c_score+=1
            elif player_choice=="paper":
                print("You win!")
                p_score+=1
        
        elif computer_choice=="paper":
            if player_choice=="rock":
                print("Computer wins!")
                c_score+=1
            elif player_choice=="scissors":
                print("You win!")
                p_score+=1
        elif computer_choice=="scissors":
            if player_choice=="rock":
                print("You win!")
                p_score+=1
            elif player_choice=="paper":
                print("Computer wins!")
                c_score=+1
            
    elif player_choice==computer_choice:
        print("Computer choice:", computer_choice)
        print("Your choice:", player_choice)
        print("Welp!", "You and the computer chose", computer_choice, "Try again!")

    print("Computer score =", c_score)
    print("Your score =", p_score)

#to end program after player wins once
''' if p_score>0:
        break'''

print("You are the final winner!")





