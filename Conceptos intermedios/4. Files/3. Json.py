""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 09/Ene/2024
"""

import json

obj = {
    "name" : "Juan Perez",
    "age": 13, 
    "Cyty": "Cali"
}

with open("/Users/Maxy/Documents/GitHub/PythonCourse/test.json", 'w') as outfile:
    #Convert to Json:
    json.dump(obj, outfile)
    
