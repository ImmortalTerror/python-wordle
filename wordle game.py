# Python "Wordle clone" game by Levi Miller for IST Y9


# Modules
# ////////////////////////////////////////////////
import wordle                                    # Wordle module from wordle.py
from os import system, name                      # For clearing screen
from time import sleep                           # For pausing
from termcolor import colored, cprint            # For printing colored text
# ////////////////////////////////////////////////



# Main game
# ////////////////////////////////////////////////

# Makes game vars
secret = wordle.genWord(5)
guess = ""
guesses = []
guessCount = 0



# Clear screen
system("cls" if name == "nt" else "clear")
# Main loop
while True:

    # If user has hit max tries
    while guessCount == 6:
        cprint("\nYou ran out of tires...", "red")
        print(colored("Would you like to try again? ", "green") + colored("(Y/N)", "yellow"))
        # Yes or no
        answer = input().lower()
        # If user chose no
        if answer == "n":
            # clear screen and exit
            system("cls" if name == "nt" else "clear")
            cprint("Thanks for playing :)", "green", attrs=["bold"])
            sleep(2)
            exit()
        # If user chose yes
        elif answer == "y":
            # Reset vars and break out of loop
            secret = wordle.genWord(5)
            guess = ""
            guesses = []
            guessCount = 0
            system("cls" if name == "nt" else "clear")
            break
        # Invalid input
        else:
            cprint("\nInvalid input...", "red")
            sleep(1)
            system("cls" if name == "nt" else "clear")
            for i in guesses: print(i)
    
    
    
    # If the word was guessed
    while guess == secret:
        cprint("\nYou guessed the word!", "green")
        print("The word was " + colored(secret, "red") + " and it took you " + colored(guessCount, "yellow") + " tries to get it.")
        print(colored("\nWould you like to try again? ", "green") + colored("(Y/N)", "yellow"))
        # Yes or no
        # This is identical to when you run out of tires
        answer = input().lower()
        # If user chose no
        if answer == "n":
            # Clear screen and exit
            system("cls" if name == "nt" else "clear")
            cprint("Thanks for playing :)", "green", attrs=["bold"])
            sleep(2)
            exit()
        # If user chose yes
        elif answer == "y":
            # reset vars and break out of loop
            guess = ""
            guesses = []
            guessCount = 0
            secret = wordle.genWord(5)
            system("cls" if name == "nt" else "clear")
            break
        # Invalid input
        else:
            cprint("\nInvalid input...", "red")
            sleep(1)
            system("cls" if name == "nt" else "clear")
            for i in guesses: print(i)


    
    # Users guess
    guess = input("")
    
    # Checks if its in the word list
    if guess not in wordle.allWords:
        cprint("\nInvalid word...", "red")
        sleep(1)
        system("cls" if name == "nt" else "clear")
        for i in guesses: print(i)
        continue

    # Try's to run match function, if a ValueError is raised, the user input a word of the wrong size
    try:
        match = wordle.match(guess, secret)
    except ValueError:
        cprint("\nInput length must be 5...", "red")
        sleep(1)
        system("cls" if name == "nt" else "clear")
        for i in guesses: print(i)
        continue



    # Adds one to the guess counter
    guessCount += 1
    # Adds users guess to the list of guesses
    guesses.append(match)
    # Clears the screen, prints the list of guesses, and go's to the start of the loop
    system("cls" if name == "nt" else "clear")
    for i in guesses: print(i)

# ////////////////////////////////////////////////