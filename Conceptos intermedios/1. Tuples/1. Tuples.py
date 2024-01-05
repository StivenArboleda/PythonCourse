""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

#Tuples are similar to lists, with the difference
#that the tuples are not modified

x = ()
print(x)

x = (1, 2, 3)
print(x)

x = 1, 2, 3
print(x)

#Tuple access
tupla = 1, 2, ('a', 'b'), 3
print(tupla)
print(tupla[2][1])

#Assignment
l = (1, 2, 3)
x, y, z = l
print(x)
print(y)

#Count repeated
l = (1, 1, 1, 3, 5)
print(l.count(1))

#In what position is that element
l = (7, 7, 7, 3, 5)
print(l.index(5))

# In what position is the element.
# First digit the number to search
# Second digit from what position
l = (7, 7, 7, 3, 5)
print(l.index(7, 1))