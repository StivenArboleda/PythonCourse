""""
Course: Desarrollo en Python Avanzado
Author: Stiven Arboleda
Date: 09/Ene/2024
"""

import pandas as pd

#df = pd.read_csv("/Users/Maxy/Documents/GitHub/PythonCourse/documents/Catalog_v2.csv")

# Acces por row
#print(df[1:5])

# Access por column

#print(df[["levelType", "code"]])

#Filter

df = pd.read_csv("/Users/Maxy/Documents/GitHub/PythonCourse/documents/Catalog_v2.csv")

filter = df['levelType'] == "CATEGORY"
df_category = df.where(filter).notna()
print(df_category)
