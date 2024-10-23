import random

secret_words = ['apple', 'banana', 'kiwi', 'orange', 'melon']

secret_word = random.choice(secret_words)

def check_guess(guess):
    """Check if the guessed letter is in the secret word."""
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    """Prompt the user for a valid letter guess."""
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()

