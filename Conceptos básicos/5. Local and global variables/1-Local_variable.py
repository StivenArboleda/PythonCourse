""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 09/Jul/2023
"""


# The local variable only works inside a function
# In this case the local variable is bandera
def numero_mayor(num1, num2):
    bandera = False
    if num1 > num2:
        bandera = True
    return bandera

x = int(input("Número 1: "))
y = int(input("Número 2: "))

if numero_mayor(x, y):
    print("El número {} es mayor a {}".format(x, y))
else:
    print("El número {} es mayor a {}".format(y, x))

#NOTE: If you want to use "bandera" outside of the function numero_mayor you will get an error