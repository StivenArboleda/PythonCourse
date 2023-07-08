""""
Curso: Principios básicos de Python
Author: Stiven Arboleda
Fecha: 08/Jul/2023
"""

'''
ADICIÓN         |   +
SUSTRACIÓN:     |   -
MULTIPLICACIÓN  |   *
DIVISIÓN        |   /   División de flotante
DIVISIÓN        |   //  División de piso
MÓDULO          |   %   
EXPONENCIACIÓN  |   **
'''

x = 100
y = 10

print("Valor de x =", x)
print("Valor de y =", y)
print("La suma de x con y =", x+y)
print("La resta de x con y =", x-y)
print("La multiplicación de x con y =", x*y)

#División flotante
x, y = 13,2 # -> Se asigna nuevos valores a X y Y por efectos del ejemplo
print("La división de x con y =", x/y)
#División de piso
print("La división de x con y exacta =", x//y)

#Módulo
x, y = 13, 2
print("El módulo de x con y =", x%y)

#Potencia
x, y = 2, 5
print("La potencia de x con y", x**y)