""""
Curso: Principios básicos de Python
Author: Stiven Arboleda
Fecha: 08/Jul/2023
"""

# TIPO DE DATO: Integer - Entero
entero = 25
print(entero)

# TIPO DE DATO: Float - Flotante - Coma decimal
pi = 3.14
print(pi)

#Boolean - lógico - Verdad o falso
bandera = True
print(bandera)
# Se puede imprimir directamente el valor
print(True)
print(False)
# Otras maneras de expresarlo
print(bool(1)) # True
print(bool(0)) #False

# TIPO DE DATO: String - Cadena de caracteres
saludo = "Hola mundo"   #Comillas dobles
saludo2 = 'Hola mundo 2'  #Comillas simples
pi = "3.14"             #Se puede expresar numéricos
print(saludo)
print(saludo2)
print(pi)

# TIPO DE DATO: Asignación es "="

z = 40
z = z + 22

# Finalmente. Queremos saber el tipo de datos de nuestras variables
print(type(entero))
print(type(pi))
print(type(bandera))
print(type(saludo))