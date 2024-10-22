
#The random module has a choice method which returns a random item from a given sequence.
import random

#Create a list containing the names of your 5 favorite fruits.
fruits = ['orange', 'apple', 'banana', 'kiwi', 'melon']

#Assign this list to a variable called word_list
word_list = fruits
print(word_list)

#Create random choice which assigns the randomly generated word to a new variable
word = random.choice(word_list)

print(word)

#Ask the user to enter a single letter
guess = input("Enter a single letter")

#Checks that the input is a single letter
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")  
else:
    print("Oops! That is not a valid input.")

