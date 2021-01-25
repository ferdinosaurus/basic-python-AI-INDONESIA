import helper
import biodata

input_menu=0
input_nama = ""
input_umur = 0
input_notelp = ""
input_alamat = ""
list_data = []

def menu1():
    input_nama = input("masukkan nama : ")
    input_umur = helper.inputInteger("masukkan umur : ",0,100)
    input_notelp = helper.inputTelp("masukkan no telp :")
    input_alamat = input("alamat : ")
    B1 = biodata.biodata(input_menu,input_umur,input_notelp,input_alamat)
    B1.printData()
    list_data.append(B1)

def menu2():
    for data in list_data:
        print
        data.printData()



while input_menu !=3:
    print("menu")
    print("1.tambah")
    print("2.tampilkan data")
    input_menu = helper.inputInteger("choose : ",1,3)

    if input_menu ==1:
        menu1()
    elif input_menu ==2 :
        menu2()

        
    