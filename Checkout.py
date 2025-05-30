#stock barang barang
print("Harga barang-barang toko")
print("Harga baju: Rp.150.000")
print("Harga celana: Rp.200.000")
print("Harga tas: Rp.250.000")
print("Harga topi: Rp.75.000")

#Input jumlah barang yang diinginkan 
#oj: opsi dan jumlah
print("Masukan Jumlah barang yang diinginkan, bila ada barang yang tidak diinginkan silahkan ketik 0")
jbaju = int(input("jumlah baju:"))
jcelana = int(input("jumlah celana:"))
jtas = int(input("jumlah tas:"))
jtopi = int(input("jumlah topi:"))

#diskon baju
def tbaju():
    global djbaju
    global htbaju
    dbaju = 0.15
    tbaju = jbaju*150000
    if jbaju >= 2:
        djbaju = tbaju*(1-dbaju)
        htbaju = print("Harga total baju setelah diskon:", djbaju)
    else:
        djbaju = tbaju*(1)
        htbaju = print("Harga total baju tanpa diskon:", djbaju)
    return htbaju
tbaju()

#diskon celana
def tcelana():
    global djcelana
    global htcelana
    dcelana = 0.15
    tcelana = jcelana*200000
    if jcelana >= 2:
        djcelana = tcelana*(1-dcelana)
        htcelana= print("Harga total celana setelah diskon:", djcelana)
    else:
        djcelana = tcelana*(1)
        htcelana = print("Harga total celana tanpa diskon:", djcelana)
    return htcelana
tcelana()

#diskon tas
def ttas():
    global djtas
    global httas
    dtas = 0.20
    ttas = jtas*250000
    if jtas >= 3:
        djtas = ttas*(1-dtas)
        httas = print("Harga total tas setelah diskon:", djtas)
    else:
        djtas = ttas*(1)
        httas = print("Harga total tas tanpa diskon:", djtas)
    return httas
ttas()

#diskon topi
def ttopi():
    global djtopi
    global httopi
    dtopi = 0.10
    ttopi = jtopi*75000
    if jtopi >= 4:
        djtopi = ttopi*(1-dtopi)
        httopi = print("Harga total topi setelah diskon:", djtopi)
    else:
        djtopi = ttopi*(1)
        httopi = print("Harga total topi tanpa diskon:", djtopi)
    return httopi
ttopi()

#RUMUS CHECKOUT JUMLAH
def harga_checkout():
    jumlahdj = djbaju + djcelana + djtas + djtopi
    global totalcheckout
    if jumlahdj >= 5000000:
        totalcheckout = jumlahdj*(1-0.05)
        print("harga checkout dengan diskon total 5%:", totalcheckout)
        if jumlahdj >= 10000000:
            totalcheckout = jumlahdj*(1-0.075)
            print("harga checkout dengan diskon total 7,5%:", totalcheckout)
    else:
        totalcheckout = jumlahdj
        print("harga checkout tanpa diskon checkout:", totalcheckout)
    return totalcheckout
harga_checkout()