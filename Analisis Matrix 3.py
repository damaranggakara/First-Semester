import pandas as pd
import numpy as np

#### anggota ####
# Damar Prana Anggakara (235091100111007)
# Dimas Setyo Adi Nugroho (235091100111013)
# Muhammad Kautsar Khaliluddin (235091100111013)

data = pd.read_csv("doc\Data_Tugas_2_PD.csv")
x = np.array(data["x"])
y = np.array(data["y"])

matrix1 =np.vstack((np.ones(len(x)), x)).T
X1_transpose_X1 = np.dot(matrix1.T, matrix1)
X1_transpose_Y = np.dot(matrix1.T, y)
beta = np.dot(np.linalg.inv(X1_transpose_X1), X1_transpose_Y)
beta_1 = beta[0]  # Intercept
beta_2 = beta[1]  # Slope

print(f"nilai awal kekuatan gear road adalah :\n{round(beta_1,2)}\n")
print(f"kenaikan/penurunan gear roda tiap bertambahnya usia dalam minggu/pekan adalah :\n{round(beta_2,2)}")
