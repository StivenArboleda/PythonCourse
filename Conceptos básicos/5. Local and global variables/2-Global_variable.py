""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 09/Jul/2023
"""
# Global variables can be used inside and outside of functions
#They are declared out of duty

PI = 3.1415

def area_circulo(radio):
    area = PI*pow(radio, 2)
    return area

radio = float(input("Radio: "))
print("El area del circulo con radio {} es {} ".format(radio, area_circulo(radio)))
print(PI)