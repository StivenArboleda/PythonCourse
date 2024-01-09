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
        
    def bark(self):
        print("Guau")
        
    def walk(self, pasos):
        print(f"Walking {pasos} pasos")
        
my_dog = Dog("Zeus", "Golden")
my_dog.bark()
my_dog.walk(10)


