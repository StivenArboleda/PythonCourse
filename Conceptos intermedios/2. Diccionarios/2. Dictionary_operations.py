""""
Course: Principios básicos de Python
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

#Access to dictionary
d1 = {
    "Nombre" : "Jorge",
    "Edad": 25,
    "Documento": 1212121
}
print(d1["Nombre"])
print(d1["Edad"])
print(d1["Documento"])

#Edition
print("Nombre antes de editar: {}".format(d1["Nombre"]))
d1["Nombre"] = "Stiven"
print("Nombre después de editar: {}".format(d1["Nombre"]))

#Add
d1["Apellido"] = "Barco"
print(d1)

#Iterate

#Print the keys
for x in d1:
    print(x)
    
#Print the values
for x in d1:
    print(d1[x])
    
#Print key and value
for x, y in d1.items():
    print(x,y)
    
# Functions of dictionaries
"""
.clear() == Clean the dictionary.
.get('a', "Not found") == looks up the value of a key. The second parameter is a default message if it is not found.
.item() = A dictionary list of all key values.
.keys() = Returns the list of all keys.
.value() = Returns the list of all values.
""" 