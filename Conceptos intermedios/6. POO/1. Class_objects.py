""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 09/Ene/2024
"""
class Dog:
    def __init__(self, name, race):
        print(f"Creating dog {name}, {race}")
        
        self.name = name
        self.race = race
        
my_dog = Dog("Zeus", "Golden")
print(my_dog.name)
print(my_dog.race)

class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

student1 = Student("Stiven", "Real", 23)
print(student1.name +" " + student1.lastname)