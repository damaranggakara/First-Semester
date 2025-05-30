# ANGGOTA :
# Damar Prana Anggakara (235091100111007) 
# A.A Gede Wiraditya Kumara Buana (235091100111006)
# Dimas Setyo Adi Nugroho (235091100111010)
# Muhammad Kautsar Khaliluddin (235091100111013)


import numpy as np
A=np.array([[10,12,9,6,8],
            [7,9,5,5,6],
            [6,5,8,2,3],
            [3,4,5,6,1],
            [12,5,6,7,23]])

B=np.array([[10,12,9],
            [7,9,5],
            [6,5,8],
            [15,6,7],
            [4,5,26]])

P = np.array([
    [5, 4, 4, 4],
    [5, 4, 3, 4],
    [4, 4, 4, 3],
    [4, 4, 4, 4],
    [4, 5, 4, 4],
    [5, 5, 4, 3],
    [4, 4, 5, 4],
    [4, 4, 3, 4],
    [3, 3, 4, 3]])


transposed_matrix = np.transpose(A)
inversed_matrix= np.linalg.inv(A)
matrix_multiplied= np.dot(A, B)
covariance_matrix = np.cov(P, rowvar=False)
dm_cvp= np.diag(covariance_matrix)
matrixp_cl1 = P[:, 0]
matrixp_cl4 = P[:, 3]
correlation = np.corrcoef(matrixp_cl1, matrixp_cl4)[0, 1]

print("transposed matrix:", transposed_matrix)
print("inverse matrix:", inversed_matrix)
print("perkalian matrix A dan B:", matrix_multiplied)
print("matrix P:", P)
print("cv matrix P:", covariance_matrix)
print("diagonal matrix P covariance:", dm_cvp)
print("korelasi P1 dan P4:", correlation)