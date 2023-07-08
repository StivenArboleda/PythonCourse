""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 08/Jul/2023
"""

'''
EQUALITY        |   ==
DIFFERENCE      |   !=
GREATER THAN    |   >
LESS THAN       |   <   
GREATER EQUAL   |   <=  
LESS EQUAL      |   >=  
'''

x, z = 30, 35

print("Igualdad entre X y Z", x == z)
print("Diferencia entre X y Z", x != z)
print("X menor que Z", x < z)
print("X mayor que Z", x > z)
print("X menor o igual que Z", x <= z)
print("X mayor o igual que Z", x >= z)

# Also applies with String

x = "Juan"
z = "Juan"

print("Igualdad entre X y Z", x == z) # It takes into account lowercase and uppercase
print("Diferencia entre X y Z", x != z)
print("X menor que Z", x < z)
print("X mayor que Z", x > z)
print("X menor o igual que Z", x <= z)
print("X mayor o igual que Z", x >= z)