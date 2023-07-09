""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

'''
STRUCTURE

if conditional:
    option1
elif conditional:
    option2
else:
    option3
'''
# Example: 
# A program is going to be created that allows to decide if a number is positive, negative or zero

number = int(input("Ingresar número: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

'''
IMPORTANT: 
If the function includes only one "if", it's simple
If the function includes an "if" and an "else" it is double
If the function includes an "if", "elif" and an "else", it is multiple
'''

# Nested conditional

age = int(input("Ingresar la edad: "))

if age >= 18:
    print("Mayor de edad")
else:
    if age > 0:
        print("Menor de edad")
    else:
        print("Edad no válida")
