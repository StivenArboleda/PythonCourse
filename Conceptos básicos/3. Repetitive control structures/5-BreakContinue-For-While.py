""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

# EXAMPLES WHILE
i = 1
while i < 10:
    print(i)
    i += i
    break #The cycle ends forced. does not increase

i = 1
while i < 10:
    print(i)
    if i == 5: 
        break #The cycle ends forced. does not increase
    i += 1

#EXAMPLE FOR
for element in range(1, 100):
    print(element)
    break

for element in range(1, 10, 1):
    if element == 5:
        continue #Does not execute the below, start again
    print(element)


