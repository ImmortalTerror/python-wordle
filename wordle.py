# Modules
from requests import get
from random import choice
from termcolor import colored



# genWord Function
# Generates random word
allWords = get("https://www.mit.edu/~ecprice/wordlist.10000").text.splitlines()

def genWord(length = 0):
    """Generates random word of given length
    If no length was given, it will do any length
    Args: Length (int)
    Returns: string"""

    correctWords = []
    
    if length != 0:
        for word in allWords:
            if len(word) == length:
                correctWords.append(word)
        
        return choice(correctWords)
    else:
        return choice(allWords)



def match(guess, word):
    """Args: guess (string), word (string)
    Returns: string"""
    # checks if args are strings
    if type(guess) != str or type(word) != str:
        raise TypeError("Both arguments must be strings")

    # Checks if args are same length
    if len(guess) != len(word):
        raise ValueError("Strings must be the same length")

# this shit still ain't work'n :(

    # for i in range(0, len(guess)):
    #     if guess[i] == word[i]:
    #         if i == 0:
    #             correct = colored(guess[i], "green")
    #         else:
    #             correct = correct + colored(guess[i], "green")
    #     else:
    #         if i == 0:
    #             correct = guess[i]
    #         else:
    #             correct = correct + guess[i]
    for i in word:
        if guess.find(i) != word.find(i):
            guess = guess.replace(i, colored(i, "yellow"))

    for i in word:
        if guess.find(i) == word.find(i):
            guess = guess.replace(i, colored(i, "green"))

    return guess



y = input()
x = input()
print(match(x, y))