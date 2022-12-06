# Modules
from random import choice  # Picks random stuff from specified list
from requests import get  # Sends get requests to websites
from termcolor import colored  # Makes colored text

# genWord Function
# Generates random word
allWords = get(
    "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
).text.splitlines()


def genWord(length=0):
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


# Adds the colores to the guess. Basically the wordle in wordle
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

    # Turns guess and word into lists of characters
    guessList = []
    for i in guess:
        guessList.append(i)
    wordList = []
    for i in word:
        wordList.append(i)

    # Finds exact matches
    for i in range(len(word)):
        if guessList[i] == wordList[i]:
            guessList[i] = colored(guessList[i], "green")

    # Finds characters that are in the word but with the wrong index
    for i in range(len(word)):
        for c in range(len(guess)):
            if wordList[i] == guessList[c] and i != c:
                guessList[c] = colored(guessList[c], "yellow")

    # Converts the list to a string and returns it
    output = ""
    for i in guessList:
        output += i

    return output
