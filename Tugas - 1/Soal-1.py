import Helper

nama = ""
umur = 0
tinggi = 0.0

tryAgain = True

print("software perkenalan : ")
print("==============================")

while tryAgain:

    #input case
    nama = str(input("masukkan nama : "))
    umur = Helper.inputInteger("masukkan umur : ")
    tinggi = Helper.inputFloat("masukkan tinggi badan : ")
    print("Nama saya {}, umur saya {} tahun dan tinggi saya {} cm.".format(nama,umur,tinggi))

    #input try Again
    value = Helper.inputYesNo("mau coba lagi ")
    tryAgain = Helper.checkYN(value)

Helper.printClosing()
