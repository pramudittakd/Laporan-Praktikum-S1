print("Latihan bagian 1")
import datetime
mahasiswa = {
    "Nama":"Nama" ,
    "NIM": 0000 ,
    "sks_lulus" : 0 ,
    "lahir":datetime.datetime(2000,1,1)
} 
data_mahasiswa ={ }
print(f"{'Selamat datang':^20}")
print(f"{'Data mahasiswa':^20}")
print("-" * 20)

mahasiswa = dict.fromkeys(mahasiswa.keys())
print(mahasiswa)

mahasiswa['Nama'] = input("Nama Mahasiswa: ")
mahasiswa['NIM'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = input("Jumlah SKS lulus: ")
tahun_lahir = int(input("Tahun lahir (yyyy): "))
bulan_lahir = int(input("Bulan lahir (1-12): "))
tanggal_lahir = int(input("Tanggal lahir (1-30): "))
mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir).strftime("%d-%m-%Y")

print(mahasiswa)

print("\n")
print("\nLatihan 2")
import datetime
import os
import random
import string

mahasiswa_template = {
    "Nama": "nama",
    "NIM": "0000",
    "prodi": "prodi",
    "sks_lulus": 0,
    "lahir": datetime.datetime(2000, 1, 1),
}

data_mahasiswa = {}

while True:
    # os.system("cls")  # utk windows
    os.system("cls")
    print(f"{'Selamat datang':^20}")
    print(f"{'Data mahasiswa':^20}")
    print("-" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["Nama"] = input("Nama Mahasiswa\t: ")
    mahasiswa["NIM"] = input("NIM Mahasiswa\t: ")
    mahasiswa["prodi"] = input("Prodi\t\t: ")
    mahasiswa["sks_lulus"] = input("SKS lulus\t: ")
    tahun_lahir = int(input("Tahun lahir (yyyy)\t: "))
    bulan_lahir = int(input("Bulan lahir (1-12)\t: "))
    tanggal_lahir = int(input("Tanggal lahir (1-31)\t: "))
    mahasiswa["lahir"] = datetime.datetime(
        tahun_lahir, bulan_lahir, tanggal_lahir
    ).strftime("%Y-%m-%d")

    key = "".join(random.choice(string.ascii_uppercase) for _ in range(6))
    data_mahasiswa.update({key: mahasiswa})

    print(
        f"\n{'key':<6} {'Nama':<17} {'NIM':<8} {'Prodi':<15} {'SKS':<10} {'lahir':<10}"
    )
    print("-" * 72)

    for key in data_mahasiswa:
        nama = data_mahasiswa[key]["Nama"]
        nim = data_mahasiswa[key]["NIM"]
        prodi = data_mahasiswa[key]["prodi"]
        sks_lulus = data_mahasiswa[key]["sks_lulus"]
        lahir = data_mahasiswa[key]["lahir"]
        print(
            f"{key:<6} {nama:<17} {nim:<8} {prodi:<15} {sks_lulus:^10} {lahir:^10}"
        )

    print("\n")
    is_done = input("Ada tambahan? (ya/tidak) :").strip().lower()
    if is_done == "tidak":
        break

print("\nAkhir dari program, terima kasih")


print ("\n")
print ("\nHasil Praktikum")

import datetime
import os
import string
import random

perpus_template ={
    'judul': 'name',
    'penulis': 'someone',
    'tahun_terbit': 0000,
    'tanggal_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'ada'
}

data_buku = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG': ^20}")
    print(f"{'DATA perpustakaan': ^20}")
    print("-"*20)
    perpus = dict.fromkeys(perpus_template.keys())
    perpus['judul'] = input("Judul buku\t: ")
    perpus['penulis'] = (input("Penulis\t: "))
    tahun_terbit = int(input("Tahun terbit (yyy)\t: "))
    bulan_terbit = int(input("Bulan terbit (1-12)\t: "))
    tanggal_terbit = int(input("Tanggal terbit (1-31)\t: "))
    perpus['tahun_terbit'] = datetime.datetime(tahun_terbit, bulan_terbit, tanggal_terbit)

    tahun_pinjam = int(input("\nTahun pinjam (yyyy)\t: "))
    bulan_pinjam = int(input("Bulan pinjam (1-12)\t: "))
    tanggal_pinjam = int(input("Tanggal pinjam (1-31)\t: "))
    perpus['tanggal_pinjam'] = datetime.datetime(tahun_pinjam, bulan_pinjam, tanggal_pinjam)
    perpus['status'] = input("\nStatus buku(ada/dipinjam): ")

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_buku.update({KEY:perpus})

    print(f"\n{'KEY': <6} {'Judul': <10} {'Penulis': <12} {'terbit': <10} {'pinjam': <15} {'Status': <8}")
    print('-' * 80)

    for perpustakaan in data_buku:
        KEY = perpustakaan
        judul = data_buku[KEY]['judul']
        penulis = data_buku[KEY]['penulis']
        terbit = data_buku[KEY]['tahun_terbit'].strftime("%x")
        pinjam = data_buku[KEY]['tanggal_pinjam'].strftime("%x")
        status = data_buku[KEY]['status']
        
        print(f"{KEY: <6} {judul: <10} {penulis: <12} {terbit: <10} {pinjam: <15} {status: <8}")

    print ("\n")
    is_done = input("Adakah tambahan buku lagi? iya/tidak: ").strip().lower()
    if is_done == "tidak":
        break

print("\nterima kasih semoga puas dengan pelayanan kami")