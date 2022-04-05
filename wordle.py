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




# String into list
def strtolist(x):
    """Turns string into list
    Args: x (string)
    Retuns: list"""

    if type(x) != str:
        raise TypeError("Input must be a string")

    output = []
    for i in x:
        output.append(i)
    return output




# List into string
def listtostr(x):
    """Turns list minto a string
    Args: x (list)
    Returns: string"""

    if type(x) != list:
        raise TypeError("Input must be a list")
    
    output = ""
    for i in x:
        output += i
    return output



def match(guess, word):
    """Colores the letters in the guess that match the word
    Args: guess (string), word (string)
    Returns: string"""
    # checks if args are strings
    if type(guess) != str or type(word) != str:
        raise TypeError("Both arguments must be strings")

    # Checks if args are same length
    if len(guess) != len(word):
        raise ValueError("Strings must be the same length")

    guessList = strtolist(guess)
    wordList = strtolist(word)

    # Finds exact matches
    for i in range(len(word)):
        if guessList[i] == wordList[i]:
            guessList[i] = colored(guessList[i], "green")

    # Finds characters that are in the word but with the wrong index
    for i in range(len(word)):
        for c in range(len(guess)):
            if wordList[i] == guessList[c] and i != c:
                guessList[c] = colored(guessList[c], "yellow")
    
        
    output = listtostr(guessList)
    
    return output