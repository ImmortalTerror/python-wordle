# Python "Wordle clone" game by Levi Miller for IST Y9

# Modules
# ////////////////////////////////////////////////
from os import system, name                     # For clearing screen
from time import sleep                          # For pausing
from termcolor import colored, cprint           # For printing colored text
import wordle                                   # Wordle module from wordle.py
# ////////////////////////////////////////////////

# Main function
def main():


    # Main game
    # ////////////////////////////////////////////////
    # Clears screen. This is just to make windows machines happy
    system("cls" if name == "nt" else "clear")

    # Main menu
    cprint("Wordle!\n", "green", attrs=["bold"])
    cprint("How to play:\n", "blue", attrs=["bold"])
    print(
        """        You have 6 attempts to guess a 5 letter word.
        Each time you guess, the letters in your guess will be colored.
        If a letter is in the word and in the correct place, it will be colored green.
        If a letter is in the word but not in the correct place, it will be colored yellow.
        If a letter is not in the word, it will not be colored.
        Any guess that is not 5 letters long will be invalid.
        Any guess that is not a valid word will be invalid.\n\n"""
        + colored("Note:", "red", attrs=["bold"])
        + " The word list is not perfect.\n      Some words may be invalid.\n"
    )
    input(colored("Press enter to continue", "green", attrs=["bold"]))

    # Makes game vars
    secret = wordle.genWord(5)
    guess = ""
    guesses = []
    guessCount = 0

    # Clear screen
    system("cls" if name == "nt" else "clear")
    print("Guesses:\n")

    # Main loop
    while True:

        # If the word was guessed
        while guess == secret:
            cprint("\nYou guessed the word!", "green")
            print(
                "The word was "
                + colored(secret, "red")
                + " and it took you "
                + colored(guessCount, "yellow")
                + " tries to get it."
            )
            print(
                colored("\nWould you like to try again? ", "green")
                + colored("(Y/N)", "yellow")
            )
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
                print("Guesses:\n")
                break
            # Invalid input
            else:
                cprint("\nInvalid input...", "red")
                sleep(1)
                system("cls" if name == "nt" else "clear")
                print("Guesses:\n")
                for i in guesses:
                    print(i)

        # If user has hit max tries
        while guessCount == 6:
            cprint("\nYou ran out of tries...", "red")
            print("The word was " + colored(secret, "green"))
            print(
                colored("\nWould you like to try again? ", "green")
                + colored("(Y/N)", "yellow")
            )
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
                print("Guesses:\n")
                break
            # Invalid input
            else:
                cprint("\nInvalid input...", "red")
                sleep(1)
                system("cls" if name == "nt" else "clear")
                print("Guesses:\n")
                for i in guesses:
                    print(i)

        # Users guess
        guess = input("").lower()

        # Checks if its in the word list
        if guess not in wordle.allWords:
            cprint("\nInvalid word...", "red")
            sleep(1)
            system("cls" if name == "nt" else "clear")
            print("Guesses:\n")
            for i in guesses:
                print(i)
            continue

        # Try's to run match function, if a ValueError is raised, the user input a word of the wrong size
        try:
            match = wordle.match(guess, secret)
        except ValueError:
            cprint("\nInput length must be 5...", "red")
            sleep(1)
            system("cls" if name == "nt" else "clear")
            print("Guesses:\n")
            for i in guesses:
                print(i)
            continue

        # Adds one to the guess counter
        guessCount += 1
        # Adds users guess to the list of guesses
        guesses.append(match)
        # Clears the screen, prints the list of guesses, and go's to the start of the loop
        system("cls" if name == "nt" else "clear")
        print("Guesses:\n")
        for i in guesses:
            print(i)
    # ////////////////////////////////////////////////


# Checks if file is being run as a script and not a module
if __name__ == "__main__":
    main()
