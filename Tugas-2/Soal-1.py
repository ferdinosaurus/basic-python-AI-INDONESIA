import Helper

input_menu =0

#data dummy
#daftar_kontak = [{'Nama':'ferdi','Telp':'081234567890'},{'Nama':'kiki','Telp':'081212121212'},{'Nama':'julius','Telp':'081987654321'}]

daftar_kontak = []


def menu_tambah_kontak():
    check_finish=False
    while check_finish==False:
        nama = input("masukkan nama :")
        telp = Helper.inputTelp("masukkan telp :")
        check_finish =Helper.add_list_dictionary(daftar_kontak,Nama = nama,Telp = telp)

while(input_menu!=3):
    Helper.printMenu()
    input_menu = Helper.inputInteger("Pilih Menu : ",1,3)

    if input_menu==1:
        Helper.printClean()
        Helper.menu_daftar_kontak(*daftar_kontak)
        input("tekan [enter] jika sudah selesai")
    elif input_menu==2:
        Helper.printClean()
        menu_tambah_kontak()
        input("tekan [enter] jika sudah selesai")
    elif input_menu==3:
        Helper.printClean()
        Helper.printClosing()
    else :
        print("Menu tidak tersedia")

