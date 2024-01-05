""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 04/Ene/2024
"""

"""
Sintaxis: 
    list = [expresion for item in iterable]
    list = [expresion for item in iterable if condition]
    
Sintaxis anidad: 
    list = [expresion for item1 in iterable for item2 in iterable] 
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
r1 = []
for item in numbers:
    value = item*2
    r1.append(value)
    
print("Listas utilizadas for normal")
print(r1)

#Por comprension
print("Listas por comprension")
r2 = [e*2 for e in numbers if e > 4]
print(r2)

######################################################

C = [[2, 3, 4],
     [40, 50, 60],
     [100, 200, 300]] 

total = 0
for row in C:
    for x in row:
        total += x
print("Listas utilizadas for normal. Caso 2")
print(total)

print("Listas por comprension. Caso 2")
total_comprension = sum([x for row in C for x in row])
print(total_comprension)