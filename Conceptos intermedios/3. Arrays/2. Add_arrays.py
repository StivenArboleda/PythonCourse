""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

matrix = []

STUDENT = 4
NOTES = 3

for i in range(STUDENT):
    notes = []
    print("STUDENT {}".format(i+1))
    for  j in range(NOTES):
        nota = float(input("Note {}: ".format(j+1)))
        notes.append(nota)
    matrix.append(notes)
    
#Route

for i in range(STUDENT):
    for j in range(NOTES):
        print(matrix[i][j], end = " ")
    print()