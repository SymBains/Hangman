import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = ['apple', 'banana', 'kiwi', 'orange', 'melon']
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower() 
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess  
            self.num_letters -= 1  
        else:
            self.num_lives -= 1  # Reduce the number of lives
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        """Ask the user to guess a letter and handle the input."""
        while True:
            guess = input("Please guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)  
                break  

ask_for_input()