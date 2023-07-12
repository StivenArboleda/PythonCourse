""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 09/Jul/2023
"""
# A module is a set of code that implements functions for a particular problem.

import math

print(math.pow(10,2))
print(math.sqrt(25))
print(math.factorial(10))
print(math.cos(45))

# the word "as" gives the module an alias
import math as mt

print(mt.pow(10,2))
print(mt.sqrt(25))
print(mt.factorial(10))
print(mt.cos(45))

from math import pow, factorial #The from keyword helps specify which functions are to be used.

print(pow(10,2))
print(factorial(10))


