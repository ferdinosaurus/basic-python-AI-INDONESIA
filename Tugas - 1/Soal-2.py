import Helper
import sys 

jari_jari = 0
tryAgain = True

print("software perhitungan lingkaran")
print("==============================")


while tryAgain:

    #input case

    jari_jari = Helper.inputFloat("masukkan jari jari :",0,sys.float_info.max)
    luas_lingkaran = Helper.luas_lingkaran(jari_jari)
    print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(jari_jari,luas_lingkaran))

    #input try Again
    value = Helper.inputYesNo("mau coba lagi ")
    tryAgain = Helper.checkYN(value)

Helper.printClosing()