# Modules bring in groups of functions, classes, and variables to make them easier to use. 
# You access them by first importing them, such as import turtle

# Copy module. This lets us copy an object

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

harry = Animal('hippogriff', 6, 'pink')

# Suppose we want a herd of these six legged pink hippogrifs. let's use the copy module
# import copy

import copy
from tkinter import ANCHOR

harriet = copy.copy(harry)

print(harry.species)
print(harriet.species)

# We can also create and copy a list of objects

bernard = Animal('dragon', 4, 'red')
carrie = Animal('chimera', 6, 'green polka dots')
billy = Animal('badger', 4, 'black stripes')

my_animals = [bernard, carrie, billy]
more_animals = copy.copy(my_animals)

print(more_animals[0].species)
print(more_animals[1].species)

# if you change a value of the original object, the copy also changes

my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)

# copy only makes a shallow copy, which means it doesn't copy objects inside the objects we copied
# Ah
# copied only the main list object, not the objects within the list
# so, we end up with a new list that does not have it's own objects- list more_animals has the same three objects inside it
# if we add a new animal to the first list, it also does not appear in the copy

sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

# Another function in the copy module is deepcopy. This creates copies of all of the objects inside the object being copied

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'
print(my_animals[0].species)
print(more_animals[0].species)

# Keeping track of keywords with the keyword module
# a Python keyword is any word in Python that is part of the language itself, such as if, else, and for. 
# The keyword module contains a function named iskeyword and a variable called kwlist
# iskeyword returns true if any string is a python keyword, and kwlist returns a list of all python keywords
# import keyword

import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)

# Getting random numbers with the random module
# the random module contains a number of functions that are useful for generating random numbers- kind of like asking the computer to pick a number
# the most useful functions in the random number module are randint, choice, and shuffle

# using randint to pick a random number
# randint picks a random number within a range

#import random

import random

print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))

# you might use randint to do something like create a simple (and annoying) guessing game using a while loop

# num = random.randint(1, 100)
# while True:
#     print('Guess a number between 1 and 100')
#     guess = input()
#     i = int(guess)
#     if i == num:
#         print('You guessed right!')
#         break
#     elif i < num:
#         print('Try higher')
#     elif i > num:
#         print('Try lower')

# using choice to pick a random item from a list
#  if you want to pick a random item from a list rather than a random number from a range, use choice

rangers = ['Jason', 'Kimberly', "Trini", 'Billy', 'Zack', 'Tommy']
print(random.choice(rangers))

# using shuffle to shuffle a list
# shuffle mixes up the items on a list

random.shuffle(rangers)
print(rangers)

# controlling the python shell with the sys module
# exiting the shell with the exit function. exit is a way of stopping the python shell or console.
# import sys

import sys

# sys.exit()

# reading with the stdin object. the stdin object (short for standard input) in the sys module prompts a user to enter
# information to be read in the shell and used by the program. This object has a readline function, which is used to 
# read a line of text typed on the keyboard until the user presses enter. it works like the input function that we used
# in the random number guessing game

# v = sys.stdin.readline()
# print(v)

# one of the differences between the input and readline function is that with readline you can specify the number
# of characters to read as a parameter

# v = sys.stdin.readline(13)
# print(v)

# writing with the stdout object
# unlike stdin, the stdout object is used to write messages to the shell (or console), rather than reading them in

sys.stdout.write('Go Go Power Rangers')

# Which version of Python am I using? The variable version displays your version of python. which can be useful if you want to make sure
# you're up to date. some programmers like to print this information when their programs start up. for example, you might put this in the
# about window of your program:

print(str(sys.version))