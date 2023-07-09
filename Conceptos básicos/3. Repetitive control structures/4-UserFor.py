""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

N = int(input("Ingresar la cantidad de alumnos: "))
for i in range(N):
    name = input("Nombre {}: ".format(i))

### SECOND EXAMPLE
# Nested for

N = int(input("Ingresar la cantidad de alumnos: "))
for i in range(N):
    name = input("Nombre {}: ".format(i))
    M = int(input("Ingrese la cantidad de cursos: "))
    for j in range(M):
        curso = input("CURSO {}:".format(j+1))
