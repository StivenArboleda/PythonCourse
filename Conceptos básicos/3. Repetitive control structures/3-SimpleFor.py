""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

#FOR LIST
elementList = [1, 2, 3, 4, 6] #A list is an element that stores data of all kinds.

for item in elementList:
    print("Este es un elemento de la lista: ", item)

#FOR STRING
#Character by character of the word
texto = "Hola mundo"
for item in texto:
    print(item)

#FOR RANGE
# Range is a reserved word
# This case is: 0 - 9
for element in range(10):
    print(element)

# This case is: 5 - 9
# The first parameter is the start and the second parameter is the end
for element in range(5, 10):
    print(element)

# This case is: 5 - 99
# The first parameter is the start, the second parameter is the end and the third parameter is jump
for element in range(5, 100, 5):
    print(element)