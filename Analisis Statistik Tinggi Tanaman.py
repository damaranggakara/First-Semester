data_rentang_tinggi_tanaman=(15, 18, 16, 20, 21,
                              12, 20, 17, 22, 20,
                                24, 24, 25, 10, 17,
                                  16, 21, 26, 30, 27,
                                    14, 15, 19, 20, 31,
                                      26, 55, 20, 15, 26,
                                        27, 23, 32, 17, 10,
                                          28, 33, 14, 29, 20)
sorted = sorted(data_rentang_tinggi_tanaman)
jumlah_data = len(data_rentang_tinggi_tanaman)
penjumlahan_data= sum(data_rentang_tinggi_tanaman)
max= max(sorted)
min= min(sorted)

import statistics as st
import numpy as np

#sorted 
print("sorted:", sorted)

#mean
jumlah_data = len(data_rentang_tinggi_tanaman)
penjumlahan_data= sum(data_rentang_tinggi_tanaman)
mean= penjumlahan_data/jumlah_data
print("mean:", mean)

#median
median = np.quantile(sorted, [0.5])
print("median:", median)

#modus
modus = st.mode(sorted)
print("modus:", modus)

#range
range= max-min
print("range:", range)

#simpangan baku
simpanganbaku= st.stdev(sorted)
print("simpangan baku:", simpanganbaku)

#Ragam
ragam= simpanganbaku*simpanganbaku
print("ragam:", ragam)

#Max
print("max:", max)

#MIN
print("min:", min)

#Q1
quartil1 =np.quantile(sorted, [0.25])
print("Q1:", quartil1)

#Q3
quartil3 =np.quantile(sorted, [0.75])
print("Q3:", quartil3)
