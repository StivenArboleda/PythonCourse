""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 05/Ene/2024
"""

#Mode 1
d1 = {
    "Nombre" : "Jorge",
    "Edad": 25,
    "Documento": 1212121
}
print(d1)

#Mode 2
d2 = dict([
    ('Nombre', 'Jorge'),
    ('Edad', 25),
    ('Documento', 12121212)
])
print(d2)

#Mode 3
d3 = dict(Nombre='Jorge',
          Edad=25,
          Documento=1212121)
print(d3)


