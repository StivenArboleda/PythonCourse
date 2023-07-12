""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 11/Jul/2023
"""

list1 = []
# None is a keyword in Python to represent nothing.
list2 = [None]

integers = [0, 1, 2, 3]
days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# A list can store different types of data in a single list
diferents = [1, "Martes", 3, True, 2.22]

# List size
print(len(integers))

# Scroll the list
for item in days:
    print(item)

for i in range(len(days)):
    print(days[i])

for i, item in enumerate(days):
    print(i, item)