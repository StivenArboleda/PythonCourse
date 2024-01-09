""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/text.txt")

linea = fichero.readline()
print(type(linea))
print(linea)
print(fichero.readline())

fichero.close()

"""Example 2"""

fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/text.txt")

sentence = fichero.readline()
while sentence != "":
    print(sentence, end="")
    sentence = fichero.readline()
    
fichero.close()
    
#Write

fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/textTwo.txt", 'w')

fichero.write("Archivo nuevo")

fichero.close()

#Write 2

fichero = open("/Users/Maxy/Documents/GitHub/PythonCourse/ListText.txt", 'w')

list = ["Apple", "pear", "orange"]

for line in list:
    fichero.write(line + "\n")

fichero.close()