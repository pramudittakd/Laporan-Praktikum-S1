#program yang menampilkan bilangan ganjil dan genap dari 1-50
print ("nomer 1\n")
#menggunakan perulangan while
angka = 1
while angka <=50:
    if angka % 2 == 0:
        print (f"{angka} itu genap")
    else:
        print(f"{angka} itu ganjil")
    angka += 1

print ("\n")

# menggunakan for... in
for i in range (1,51) :
    if i % 2 == 0 :
        print (f"{i} adlh bil genap")
    else :
        print (f"{i} adlh bil ganjil")

#program yang menampilkan semua bilangan prima dari 1-100
print ("nomer 2\n")
#menggunakan for..in
for angka in range (2, 101) :
    angka_prima = True
    for dibagi in range (2, angka) :
        if angka % dibagi == 0 :
            angka_prima = False
            break
    if angka_prima :
        print (angka, "adlh bil prima")

print ("\n")

#menggunakan while
nomer = 2
while nomer <=100 :
    pembagi = 2
    prima = True

    while pembagi < nomer :
        if nomer % pembagi == 0 :
            prima = False
            break
        pembagi +=1
    if prima :
        print (nomer, end="\n")
    nomer +=1
