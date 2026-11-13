print ("Nomer 1\n")
print ("a.")
#membuat tuple mahasiswa
mahasiswa = ("pramuditta Kemala", 2605060047, "Teknologi Imfomasi")
print (f"data lama :{mahasiswa}")
print ("b.")
#menampilkan data nim dan prodi dengan mengakses indeks
print (f"Nim : {mahasiswa [1]}")
print (f"Podi : {mahasiswa [2]}")
#print ("c.")
#menjalankan perintah dibawah
#mahasiswa [2] = "Mesin"
#print (f"data baru : {mahasiswa}")
print ("d.")
#membuat set
nilai = {10, 4, 3, 2, 4, 10, 7, 5}
print (nilai)


print ("\nNomer 3")
#Dictionary keranjang buah dan harganya
buah = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000, 
    "anggur" : 15000
}
total_belanja = 0
#perulangan untuk menampilkan barang dan harga
for buah,harga in buah.items () :
    print (f"Harga {buah} : Rp {harga}")
    total_belanja += harga
#untuk menampilkam total belanja
print (f"total belanja = Rp {total_belanja}")

