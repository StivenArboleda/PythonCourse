""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 09/Ene/2024
"""

import json

"""  
with open("/Users/Maxy/Documents/GitHub/PythonCourse/berry.json", 'r') as json_file:
    data = json.load(json_file)
    dictionary = data[1]
    #print(data)
    
    #print('name:', dictionary['name'])
    #print('url:', dictionary['url'])
    """
""" Example 2 """

with open("/Users/Maxy/Documents/GitHub/PythonCourse/berry.json", 'r') as json_file:
    data = json.load(json_file)
    
print(json.dumps(data, indent=2))