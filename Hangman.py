import random
from select import select

#List of Words
word_list = ["bull", "sheep", "cow"]

#Selecting a word randomly
selected_word = random.choice(word_list)

#Creating as many blanks as the letters in the word.
display_list = []
for n in selected_word:
    display_list.append("_")

#Guess a word
guessed_letter = input("Guess a letter: ").lower()

#Check if the letter exists in the word and replace in list
n = -1

for x in selected_word:
    n = n+1
    if guessed_letter == x:
        display_list[n] = guessed_letter

print (display_list)