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