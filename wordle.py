# THIS I A WIP


# Modules
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
    """Generates a random word of a given length
    Args: length (int)
    Returns: string
    default length is 5"""
    
    print("Generating word...")
    r = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    allWords = r.text.splitlines()
    word = random.choice(allWords)
    while len(word) != length:
        word = random.choice(allWords)
    return word

# Function to turn string into list
def lenlist(string):
    """Turns a string into a list of characters
    Args: string
    Returns: list"""
    wordChars = []
    for i in string:
        wordChars.append(i)
    return wordChars

# Gets characters that are an exact match
def exactMatch(a, b):
    """Compares two lists to see if they have any matching letters with the same index
    Args: a (list), b (list)
    Returns: string"""
    # if a or b != type(str):
    #     raise TypeError("Both arguments must be strings")

    if len(a) != len(b):
        raise ValueError("Strings must be the same length")

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
def parMatch(a, b):
    """Compares two lists to see if they have any matching letters without the same index
    Args: a (string), b (string)
    Returns: string"""
    if a or b != type(str):
        raise TypeError("Both arguments must be strings")
    
    if len(a) != len(b):
        raise ValueError("Strings must be the same length")

    correct = ""

    for i in b:
        for c in range(0, len(a)):
            if a[c] == i and a[c] != b[c]:
               correct = correct + colored(a[c], "yellow")
            elif a[c] != i and a[c] != b[c]:
                correct = correct + a[c]
    return correct
            


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
