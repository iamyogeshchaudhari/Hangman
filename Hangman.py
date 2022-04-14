import random
import Hangman_art

print (Hangman_art.logo)

#List of Words
word_list = ["bull", "sheep", "cow"]

#Selecting a word randomly
selected_word = random.choice(word_list)

#Creating as many blanks as the letters in the word.
display_list = []
for n in selected_word:
    display_list.append("_")

#Definitions
n = -1
user_lives = 6
game_ended = False

#Creating a loop until the user guesses all words, or exhausts all lives.
while game_ended == False:

    guessed_letter = input("Guess a letter: ").lower()

    # Check if the letter exists in the word and replace in list, or cost a life.
    if guessed_letter not in selected_word:
        user_lives = user_lives - 1

    for x in selected_word:
        n = n+1
        if guessed_letter == x:
            display_list[n] = guessed_letter
    
    n = -1

    if "_" not in display_list or user_lives == 0:
        game_ended = True
    
    print (display_list)

if "_" not in display_list:
    print("You won.")
elif user_lives:
    print("You lost. The word was" + selected_word)