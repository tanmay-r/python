import random
import string

from Words import words

def valid_word(words):
    c_word=random.choice(words).upper()
    while '-' in c_word or ' ' in c_word or len(c_word)>10:
        c_word=random.choice(words)
    return c_word
    

def hangman():
    c_word=valid_word(words)
    letters_in_word=set(c_word)
    alphabet=set(string.ascii_uppercase)
    letters_used=set()

    lives=10
    while letters_in_word!=set() and lives>0:
        print(f"Lives remaining: {lives}")
        letter_list=[letter if letter in letters_used else '_' for letter in c_word]
        print("Current word: ", " ".join(letter_list))
        print(f"You have used these letters: ", " ".join(letters_used))
        user_input=input("Enter a letter: ").upper()

        if user_input in alphabet and user_input not in letters_used:
            letters_used.add(user_input)
            if user_input in letters_in_word:
                letters_in_word.remove(user_input)
            else:
                lives-=1
                print("Your letter is not in the word!")
        elif user_input in letters_used:
            print("You have already used the letter! Use another letter.")
        else:
            print("Invalid charecter!")
    if lives == 0:
        print("Sorry, you have no lives remaining.")
        print(f"Your word was {c_word}")
    else:
        print(f'You have guessed the word!{c_word}')



    

   
   

    
valid_word(words)
hangman()







