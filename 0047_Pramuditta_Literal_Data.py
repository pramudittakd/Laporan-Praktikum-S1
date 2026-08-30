#Membuat Daftar
print("NO.1")
data_string="Pramuditta Kemala Devi"
print("Nama :",data_string)
data_integer=18
print("Usia :",data_integer)
data_float=45.8
print("Berat:",data_float)

#Mengubah Tipe Data (Konversi data)
print("\nNO.2")
#1. Konversi angka_string menjadi integer
angka_str="123"
angka_int = int(angka_str)
print("angka=", angka_int, "type=", type(angka_int))
#2. Konversi angka_float menjadi integer
angka_float= 45.67
angka_int = int(angka_float)
print("angka=", angka_int, "type=", type(angka_int))
#3. Konversi angka_integer menjadi float
angka_int= 89
angka_float = float(angka_int)
print("angka=", angka_float, "type=", type(angka_float))
#4. Konversi angka_integer menjadi string
angka_int= 89
angka_str = str(angka_int)
print("angka=", angka_str, "type=", type(angka_str))

#Mengambil Input Data dr User
print("\nNO.3")
#Menginput dgn integer
usia =  int(input("usia:"))
print(int, type(usia))
#Menginput dgn floa
tinggi_badan = float(input("TB:"))
print(float, type(tinggi_badan))
#Menginput dgn string
nama = str (input("nama:"))
print(str, type(nama))