# THIS I A WIP


# Modules
# ////////////////////////////////////////////////
from os import system, name
import wordle
# ////////////////////////////////////////////////



# Main game
# ////////////////////////////////////////////////

word = wordle.genWord(verbose = False)
system("cls" if name == "nt" else "clear")

print(word)
guess = input()

print(wordle.exactMatch(guess, word))
print(wordle.parMatch(guess, word))
input()

# ////////////////////////////////////////////////