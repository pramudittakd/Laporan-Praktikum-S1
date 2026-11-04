print ("Nomer 1.")
kendaraan = ['motor', 'mobil','sepeda', 'bus']
# a. sisipkan 'truk' diakhir list
kendaraan.append ('truk')
print (f"A. data baru ; {kendaraan}")
# b. sisipkan 'becak' pada index pertama
kendaraan.insert (1,'becak')
print (f"B. data baru ; {kendaraan}")
# c. menghapus data yang paling belakang
kendaraan.pop ()
print (f"C. data baru ; {kendaraan}")
# d. ubah elemen sepeda menjadi skuter
kendaraan [3] = 'skuter'
print (f"D. data baru ; {kendaraan}")
# e. informasi jumlah total data dalam list
banyak_data = len(kendaraan)
print (f"E. jumlah data ; {banyak_data}")

print ("\nNomer 2.")
angka = [75,80,90,75,85,100,65]
# a. mencari index data 100
posisi = angka.index(100)
print (f"A. 100 ada di index ; {posisi}")
# b. menghitung ada berapa banyak siswa dengan nilai 75
jumlahNilai = angka.count(75)
print (f"B. yang mendapatkan nilai 75 ; {jumlahNilai}")
# c. mengurutkan dari yang terkecil
angka.sort ()
print (f"C. data baru ; {angka}")
# d. membalikan urutan list
angka.reverse()
print (f"D. data baru ; {angka}")

print ("\nNomer 3.")
menu_utama = ["Nasi Goreng", "Mie Ayam"]
tambahan = ["Kerupuk", "Es Teh"]
#menggabungkan data
menu_utama.extend (tambahan)
print (f"data gabungan ; {menu_utama}")

print ("\nNomer 4.")
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
# a. menampilkan harga pensil dan memanggil indeks baris dan kolom
pensil = data_barang [1][1]
print (f"A. harga pensil ; {pensil}")
# b. perulangan untuk membaca data lalu menampilkan output dengan format yang sesuai
print ("B. Nama barang dan harga\n")
for barang in data_barang :
    print (f"Nama ; {barang [0]}")
    print (f"Harga ; {barang[1]}\n")