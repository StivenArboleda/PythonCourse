""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

# Finite loop

#First print and then increment the value of the variable, its previous value plus 1

iterator = 0
while iterator < 10:
    print(iterator)
    iterator = iterator + 1

# Infinite loop
iterator = 0
while True:
    print(iterator)
    iterator = iterator + 1