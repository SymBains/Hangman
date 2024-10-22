
#The random module has a choice method which returns a random item from a given sequence.
import random

#Create a list containing the names of your 5 favorite fruits.
favourite_fruits = ['orange', 'apple', 'banana', 'kiwi', 'melon']

#Assign this list to a variable called word_list
fruit_list = favourite_fruits
print(fruit_list)

#Create random choice which assigns the randomly generated word to a new variable
selected_fruit = random.choice(fruit_list)

print(selected_fruit)

#Ask the user to enter a single letter
user_guess = input("Enter a single letter: ")

#Checks that the input is a single letter
if len(user_guess) == 1 and user_guess.isalpha():
    print("Good guess!")  
else:
    print("Oops! That is not a valid input.")

#Refactoring to separate fuctions 
def get_favorite_fruits():
    """Return a list of favorite fruits."""
    return ['orange', 'apple', 'banana', 'kiwi', 'melon']

def select_random_fruit(fruit_list):
    """Select a random fruit from the provided list."""
    return random.choice(fruit_list)

def get_user_guess():
    """Ask the user to enter a single letter."""
    return input("Enter a single letter: ")  

def is_valid_guess(guess):
    """Check if the input is a valid single letter."""
    return len(guess) == 1 and guess.isalpha()