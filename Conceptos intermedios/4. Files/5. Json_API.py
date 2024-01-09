""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 09/Ene/2024
"""

import requests
import json

name = input("Input name: ")

url="https://api.nationalize.io/?name=" + name

result = requests.get(url).json()

print(json.dumps(result, indent=2)) 