""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

N = int(input("Ingrese la cantidad de nombres: "))

i = 1
while N >= i:
    nombre = input("Nombre {}: ".format(i)) #In this case, the {} will change to the value of the i, thanks to the format
    i += 1

### SECOND EXAMPLE
# Nested while

print("OTHER EXAMPLE")
N = int(input("Ingrese la cantidad de nombres: "))

i = 1
while N >= i:
    nombre = input("ALUMNO {}: ".format(i)) #In this case, the {} will change to the value of the i, thanks to the format
    M = int(input("Ingresar cantidad de cursos que está viendo: "))
    j = 0
    while M > j:
        curso = input("CURSO {}: ".format(j+1))
        j +=1
    i += 1