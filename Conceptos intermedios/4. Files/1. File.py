""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

#'r': Default. To read files
#'w': To write files

#Open files
#fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/text.txt")
fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/text.txt", 'r')

#Read files
print(fichero.read())

#Close files
fichero.close()


## EDIT FILES
fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/text.txt", 'w')

#Read files
print(fichero.read())

#Close files
fichero.close()