# Import
import numpy as np
import json as js

# Import File
data= open("matriks_vektor.json", "r")
ldata= js.load(data)

# Variabel matriks dan vektor
m= np.array(ldata['M'])
print(f"Matariks yang digunakan: \n{m}")
v= np.array(ldata['V'])
print("Vektor yang digunakan:", v)

# transpos matiks
transposed_matrix = np.transpose(m)
print(f"Hasil Transpose Matriks: \n{transposed_matrix}")

# perkalian vektor dan matriks
perkalianvm = np.dot(m,v)
print("Hasil Perkalian Vektor dengan Matriks:", perkalianvm)