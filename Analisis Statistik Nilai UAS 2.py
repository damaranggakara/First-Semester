#DATA NILAI UJIAN PRAKTIK FISIKA SMAN 1 MUHAMMADIYAH MALANG
Hafiz = 78
Qohar = 89
Niyasin = 85
Radith = 84
Rizki = 77 
Nifta = 81
Aisya = 72
Fatimah = 89
Nabilah = 72
Haydar = 82
Rifki = 88
Khalisa = 79
Nadine = 86
Ridho = 89
nilai_ujian_praktik = (Hafiz, Qohar, Niyasin, Radith, Rizki, 
                       Nifta, Aisya, Fatimah, Nabilah, Haydar, 
                       Rifki, Khalisa, Nadine, Ridho)
import statistics as st
import numpy

# SORTED
s = sorted(nilai_ujian_praktik)
print("Sorted :", s)

# RATA-RATA
penjumlahan = (sum(nilai_ujian_praktik))
jumlah_data = (len(nilai_ujian_praktik))
mean = penjumlahan/jumlah_data
print("Rata-rata :", mean)

# MEDIAN
z = sorted(nilai_ujian_praktik)
me = numpy.quantile(z, [0.5])
print("MEDIAN :",me)

# QUARTIL BAWAH
a = sorted(nilai_ujian_praktik)
qb= numpy.quantile(a, [0.25])
print("Quartil Bawah :", qb)

# QUARTIL ATAS
b = sorted(nilai_ujian_praktik)
qa= numpy.quantile(b, [0.75])
print("Quartil Atas :", qa)

#DESIL
pe= sorted(nilai_ujian_praktik)
jumlah_data = (len(nilai_ujian_praktik))
decile_indicate= [int(jumlah_data * (i / 10)) for i in range(1, 10)]
deciles = [pe[i] for i in decile_indicate]
print("Desil :", deciles)

#PERSENTIL 
PYD = 50 #perseintil ke 50
Hasil_Persentil = numpy.percentile(nilai_ujian_praktik,PYD)
print("Persentil :", Hasil_Persentil)

# MODUS
p = sorted(nilai_ujian_praktik)
mo = st.mode(p)
print("Modus :",mo)

# NILAI MAKSIMUM DAN MINIMUM
print("NILAI MINIMUM")
x = min(nilai_ujian_praktik)
print("Min :", x)

print("NILAI MAKSIMUM")
y = max(nilai_ujian_praktik)
print("Max :", y)

# STANDAR DEVIASI
u = sorted(nilai_ujian_praktik)
sd = st.pstdev(u)
print("Standar Deviasi :", sd)

#RAGAM
h = sd**2
print ("Ragam :", h)
