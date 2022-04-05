# THIS I A WIP


# Modules
# ////////////////////////////////////////////////
import wordle
from os import system, name
from time import sleep
from termcolor import colored, cprint
# ////////////////////////////////////////////////



# Main game
# ////////////////////////////////////////////////
secret = wordle.genWord(5)
guess = ""
guesses = []
guessCount = 0


system("cls" if name == "nt" else "clear")
while True:
    while guessCount == 6:
        cprint("\nYou ran out of tires...", "red")
        print(colored("Would you like to try again? ", "green") + colored("(Y/N)", "yellow"))
        answer = input().lower()
        if answer == "n":
            system("cls" if name == "nt" else "clear")
            cprint("Thanks for playing :)", "green", attrs=["bold"])
            sleep(2)
            exit()
        elif answer == "y":
            secret = wordle.genWord(5)
            guess = ""
            guesses = []
            guessCount = 0
            system("cls" if name == "nt" else "clear")
            break
        else:
            cprint("\nInvalid input...", "red")
            sleep(1)
            system("cls" if name == "nt" else "clear")
            for i in guesses: print(i)
    while guess == secret:
        cprint("\nYou guessed the word!", "green")
        print("The word was " + colored(secret, "red") + " and it took you " + colored(guessCount, "yellow") + " tries to get it.")
        print(colored("\nWould you like to try again? ", "green") + colored("(Y/N)", "yellow"))
        answer = input().lower()
        if answer == "n":
            system("cls" if name == "nt" else "clear")
            cprint("Thanks for playing :)", "green", attrs=["bold"])
            sleep(2)
            exit()
        elif answer == "y":
            guess = ""
            guesses = []
            guessCount = 0
            secret = wordle.genWord(5)
            system("cls" if name == "nt" else "clear")
            break
        else:
            cprint("\nInvalid input...", "red")
            sleep(1)
            system("cls" if name == "nt" else "clear")
            for i in guesses: print(i)

    guess = input("")
    if guess not in wordle.allWords:
        cprint("\nInvalid word...", "red")
        sleep(1)
        system("cls" if name == "nt" else "clear")
        for i in guesses: print(i)
        continue

    try:
        match = wordle.match(guess, secret)
    except ValueError:
        cprint("\nInput length must be 5...", "red")
        sleep(1)
        system("cls" if name == "nt" else "clear")
        for i in guesses: print(i)
        continue

    guessCount += 1
    guesses.append(match)
    system("cls" if name == "nt" else "clear")
    for i in guesses: print(i)

# ////////////////////////////////////////////////
