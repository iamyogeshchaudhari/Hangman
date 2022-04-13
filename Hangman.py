import random
from select import select

#List of Words
word_list = ["bull", "sheep", "cow"]

#Selecting a word randomly
selected_word = random.choice(word_list)

#Creating as many blanks as the letters in the word.
display_list = []
for n in selected_word:
    display_list.append["_"]

