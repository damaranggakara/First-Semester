# Import
import numpy as np
import json as js

# Import File
data= open("UAP MATRIX.json", "r")
ldata= js.load(data)

# Variabel matriks
m1= np.array(ldata['M1'])
print(f"Matariks pertama yang digunakan: \n{m1}")
m2= np.array(ldata['M2'])
print(f"Matariks kedua yang digunakan: \n{m2}")

# Hasil perkalian
m1m2= np.dot(m1, m2)
print(f"Hasil perkalian antara matix: \n{m1m2}")