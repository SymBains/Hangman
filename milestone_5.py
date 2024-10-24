import random

word_list = ['apple', 'banana', 'kiwi', 'orange', 'melon']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the attributes for the Hangman game."""
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))

    def _update_word_guessed(self, guess):
        """Update the displayed word with the guessed letter."""
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess 

    def _is_guess_correct(self, guess):
        """Check if the guessed letter is in the word."""
        return guess in self.word

    def _handle_correct_guess(self, guess):
        """Handle logic for a correct guess."""
        print(f"Good guess! '{guess}' is in the word.")
        self._update_word_guessed(guess)
        self.num_letters -= 1

    def _handle_incorrect_guess(self, guess):
        """Handle logic for an incorrect guess."""
        self.num_lives -= 1
        print(f"Sorry, '{guess}' is not in the word. You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        """Evaluate the guessed letter and update game state accordingly."""
        guess = guess.lower()
        if self._is_guess_correct(guess):
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        """Ask the user to guess a letter and handle the input."""
        while True:
            guess = input("Please guess a letter: ").lower()
            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)  
                self.check_guess(guess)  
                break  

    def _is_valid_guess(self, guess):
        """Check if the guess is a valid single alphabetical character."""
        return len(guess) == 1 and guess.isalpha()

def play_game(word_list):
    """Function to run the Hangman game."""
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game.word)
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

if __name__ == "__main__":
    play_game(word_list)
