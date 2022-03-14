from termcolor import colored

def lenlist(string):
    """Turns a string into a list of characters
    Args: string
    Returns: list"""
    wordChars = []
    for i in string:
        wordChars.append(i)
    return wordChars

def parMatch(guess, word):
    """Compares two lists to see if they have any matching letters without the same index
    Args: a (string), b (string)
    Returns: string"""
    # if a or b != type(dict):
    #     raise TypeError("Both arguments must be lists")
    
    if len(guess) != len(word):
        raise ValueError("List must be the same length")

    correct = ""
    gc = 0
    wc = 0
    for i in guess:
        for c in word:
            if i == c and gc != wc:
                correct = correct + colored(i, "yellow")
            elif i != c and gc != wc:
                correct = correct + i
            wc =+ 1
        gc =+ 1


# if guess[c] == word[i] and guess[c] != word[c]:
#     correct = correct + colored(guess[c], "yellow")
# elif guess[c] != word[i] and guess[c] != word[c]:
#     correct = correct + guess[c]
            
    return correct

guess = "ahoaa"
word = "hello"
guessl = lenlist(guess)
wordl = lenlist(word)
print(guessl)
print(wordl)
print(parMatch(guessl, wordl))