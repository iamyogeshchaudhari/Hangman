import random
import Hangman_art
import Hangman_words

#Printing hangman art logo.
print (Hangman_art.logo) 

#Definitions:
word_list = Hangman_words.word_list #list of words.
n = int(-1) #position
user_lives = 6
game_ended = False

#Selecting a word randomly.
selected_word = random.choice(word_list) 

#Creating as many blanks as the letters in the word.
display_list = []
for o in selected_word:
    display_list.append("_")

#Creating a loop until the user guesses all words, or exhausts all lives.
while game_ended == False:
    guessed_letter = input("\nGuess a letter: ").lower()

    #Check if the letter exists in the word and replace in list, or cost a life. (in reverse order)
    if guessed_letter not in selected_word:
        user_lives = user_lives - 1

    for x in selected_word:
        n = n + 1
        if guessed_letter == x:
            display_list[n] = guessed_letter

    n = -1 #Resetting value of n to -1.

    #Stopping the loop after all letters revealed, or all lives done.
    if "_" not in display_list or user_lives == 0:
        game_ended = True
    
    #Printing List and ASCII art for lives after every turn.
    print (display_list)
    print(Hangman_art.stages[user_lives]) 

#Printing if the player won or lost.
if "_" not in display_list:
    print("You won.")
elif user_lives == 0:
    print("You lost. The word was " + selected_word)