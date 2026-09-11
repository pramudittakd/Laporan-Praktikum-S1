#menginput data user berupa usia untuk dikategorikan.
usia = float(input('usia: '))
if usia == usia >= 0 and usia <= 12:
    print ("Anak-anak")
elif usia == usia >= 13 and usia <= 17:
    print ("Remaja")
elif usia == usia >= 18 and usia <= 59:
    print ("Dewasa")
else :
    print ("Lansia")