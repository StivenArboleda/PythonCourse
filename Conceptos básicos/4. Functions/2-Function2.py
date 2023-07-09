""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 09/Jul/2023
"""

# Various returns
def calculadora(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    return suma, resta, multiplicacion

#Variable "a" is equal to the first return "addition", 
#variable "b" with subtraction, 
#variable "c" with multiplication

a, b, c = calculadora(10, 5) 
print(a, b, c)


# Defined parameters

def area_circulo(radio, pi=3.14):
    area = pi*pow(radio, 2)
    return area

print(area_circulo(2)) #A single parameter because the second parameter is defined
print(area_circulo(2, 3.1415)) #If I send the second parameter, it overwrites it
