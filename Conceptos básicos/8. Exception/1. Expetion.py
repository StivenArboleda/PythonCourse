""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 04/Ene/2024
"""

try:
    resultado = 10 * (1/0)
except:
    print("Error de ZeroDivisionError")
    
try:
    spam="hola"
    print(4 + spam*3)
except:
    print("Error de NameError")
    
try:
    resultado = '2' + 2
except: 
    print("Error de TypeError")

