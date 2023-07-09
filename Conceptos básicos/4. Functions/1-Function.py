""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 09/Jul/2023
"""

def name_funcion():
    print("Esta es una función")

name_funcion() #Called to execute the function

#Inside the parentheses is called parameters
def suma(a, b):
    suma = a + b
    return suma

def resta(a, b):
    resta = a -b
    return resta

def multiplicacion(a, b):
    multiplicacion = a * b
    return multiplicacion

print(suma(5, 2)) #To call a function with parameters, you must add the corresponding values

def sumaInput():
    a = int(input("Digite un número para sumar: "))
    b = int(input("Digite un número para sumar: "))
    suma = a + b
    return suma

print(sumaInput())

#Another way


def sumaInput2():
    a = int(input("Digite un número para sumar: "))
    b = int(input("Digite un número para sumar: "))
    suma = a + b
    print(suma)

sumaInput2()

def calculadora(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    return suma, resta, multiplicacion

#Variable "a" is equal to the first return "addition", 
#variable "b" with subtraction, 
#variable "c" with multiplication

a, b, c = calculadora(10, 5) 
print(a, b, c)