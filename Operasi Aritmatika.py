#Latihan Operasi Aritmatika
panjang = 12
lebar = 5
tinggi = 8

print ("A.")
#menghitung luas balok
luas = 2*(panjang*lebar+panjang*tinggi+lebar*tinggi)
print ("luas = ", luas)
#menghitung Volume
volume = panjang*lebar*tinggi
print ("volume = ", volume)
#menghitung keliling
keliling = 4*(panjang+lebar+tinggi)
print ("keliling = ", keliling)

# Operasi komperasi
print ("\nB.")
#Apakah luas bangunan tersebut lebih luas dari 50? 
hasil_b = luas > 50
print (hasil_b)

print ("\nC.")
#Apakah volume tersebut bernilai 480? 
hasil_c = volume == 480
print (hasil_c)

#pada operasi komperasi, hasilnya akan membentuk tipe data boolean yang menampilkan true or false
#untuk membuktikannya bisa menggunakan 'type'
print ("\nContoh")
print (hasil_b, type(hasil_b))
print (hasil_c, type(hasil_c))