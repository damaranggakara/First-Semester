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
data = [Hafiz, Qohar, Niyasin, Radith, Rizki, Nifta, Aisya, Fatimah, 
        Nabilah, Haydar, Rifki, Khalisa, Nadine, Ridho]

#RATA-RATA
for i in data:
    total = 0
    total = total + i
mean = total/14
print("RATA-RATA :", mean)

#MAX
max = data[0]
for i in data:
    if max < i:
        max = i
print("MAX :", max)

#MIN
min = data[0]
for i in data:
    if min > i:
        min = i
print("MIN :", min)

#URUTAN DATA
def bubble(data):
    index = len(data)-1
    for i in range(index, -1, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
bubble(data)
print("URUTAN :", data)

#KUARTIL 1
bubble(data)
n = int(((14+2)/4)-1)
letak = data[n]
print("KUARTIL 1 :", letak)

#KUARTIL 2 (MEDIAN)
bubble(data)
n = int((((14/2)+(14/2+1))/2)-1)
p = n
q = n + 1
med = int((data[p]+data[q])/2)
print("KUARTIL 2 :", med)

#KUARTIL 3
bubble(data)
n = int((((3*14)+2)/4)-1)
letak = data[n]
print("KUARTIL 3 :", letak)

#DESIL
bubble(data)
i = int(input('Desil ke- :'))
x = ((i*(14+1))/10)
if i  % 2 == 1:
    z = 0.5
else:
    z=1
y = (data[int(x-1)])+z*(int(data[int(x)]-data[int(x-1)]))
print("LETAK DESIL :", x)
print("NILAI DESIL :", y)

#PERSENTIL
bubble(data)
i = int(input('Persentil ke- :'))
x = ((i*(14+1))/100)
if i  % 2 == 1:
    z = 0.5
else:
    z=1
y = (data[int(x-1)])+z*(int(data[int(x)]-data[int(x-1)]))
print("LETAK PERSENTIL :", x)
print("NILAI PERSENTIL :", y)




        

