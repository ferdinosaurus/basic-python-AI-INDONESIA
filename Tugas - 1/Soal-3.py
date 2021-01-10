import Helper


nilai_ujian =0.0
nilai_praktek =0.0

tryAgain = True

print("software pengecheckan kelulusan siswa")
print("==============================")

while tryAgain:

    #input case
    nilai_ujian = Helper.inputFloat("masukkan nilai ujian: ")
    nilai_praktek = Helper.inputFloat("masukkan nilai praktek: ")
    
    
    if nilai_ujian>=70 and nilai_praktek>=70:
        print("Selamat, anda lulus!")
    elif nilai_ujian>=70 and nilai_praktek<70:
        print("Anda harus mengulang ujian praktek.")
    elif nilai_ujian<70 and nilai_praktek>=70:
        print("Anda harus mengulang ujian teori.")
    else :
        print("Anda harus mengulang ujian teori dan praktek.")

    #input try Again
    value = Helper.inputYesNo("mau coba lagi ")
    tryAgain = Helper.checkYN(value)

Helper.printClosing()