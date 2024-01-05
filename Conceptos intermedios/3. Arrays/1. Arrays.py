""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

matrix = []

FILAS = 4
COLUMNAS = 6

for i in range(FILAS):
    fila = [0] * COLUMNAS
    matrix.append(fila)
    
print(matrix)

pbi = [[2.9, 2.5], [3.9, 4.0], [0.9, 2.2], [1.5, 3.3],
       [1.8, 2.6], [1.0, 2.0], [2.2, 2.3], [4.0, 4.0],
       [2.5, 3.5], [3.0, 3.0], [-9.5, -0.5]]

FILAS = 11
COLUMNAS = 2

for i in range(FILAS):
    for j in range(COLUMNAS):
        print(pbi[i][j], end = " ")
    print()
    
item = pbi[2][1] # [i][j] ---> i: fila, j: columna
print(item)