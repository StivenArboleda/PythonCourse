""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

'''
ADDITION         |   +
SUBSTRATION      |   -
MULTIPLICATION   |   *
DIVISION         |   /   Floating division
DIVISION         |   //  Floor division
MODULE           |   %   
EXPONENTIATION   |   **
'''

x = 100
y = 10

print("Valor de x =", x)
print("Valor de y =", y)
print("La suma de x con y =", x+y)
print("La resta de x con y =", x-y)
print("La multiplicación de x con y =", x*y)

#Floating division
x, y = 13,2 # -> New values ​​are assigned to X and Y for purposes of the example
print("La división de x con y =", x/y)
#Floor division
print("La división de x con y exacta =", x//y)

#Module
x, y = 13, 2
print("El módulo de x con y =", x%y)

#Potency
x, y = 2, 5
print("La potencia de x con y", x**y)