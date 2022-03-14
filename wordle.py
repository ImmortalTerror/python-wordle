# THIS I A WIP


# Moduals
# ////////////////////////////////////////////////
import requests
import random
import os
from termcolor import colored
# ////////////////////////////////////////////////



# Functions
# ////////////////////////////////////////////////

# Random word function
def genWord(length = 5):
    print("Generating word...")
    r = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    allWords = r.text.splitlines()
    word = random.choice(allWords)
    while len(word) != length:
        word = random.choice(allWords)
    return word

# Function to turn string into list
def lenlist(string):
    wordChars = []
    for i in string:
        wordChars.append(i)
    return wordChars

# Gets characters that are an exact match
def exactMatch(a, b):
    if len(a) != len(b):
        return -1

    for i in range(0, len(a)):
        if a[i] == b[i]:
            if i == 0:
                correct = colored(a[i], "green")
            else:
                correct = correct + colored(a[i], "green")
        else:
            if i == 0:
                correct = a[i]
            else:
                correct = correct + a[i]
    return correct

# Compares two words to see if they have any matching letters
# figure this shit out later :)
# ////////////////////////////////////////////////



# Main game
# ////////////////////////////////////////////////

word = genWord()
os.system("cls" if os.name == "nt" else "clear")

print(word)
guess = input()

guessChars = lenlist(guess)
wordChars = lenlist(word)

print(guessChars)
print(wordChars)

print(exactMatch(guessChars, wordChars))
input()

# ////////////////////////////////////////////////
