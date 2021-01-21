import Helper

input_menu =0
daftar_kontak = [{'Nama':'ferdi','Telp':'081234567890'}]

def menu_tambah_kontak():
    check_finish=False
    while check_finish==False:
        nama = input("masukkan nama :")
        telp = Helper.inputTelp("masukkan telp :")
        check_finish =Helper.add_list_dictionary(daftar_kontak,Nama = nama,Telp = telp)
    

def menu_cari_kontak():
    search = input("masukkan pencarian : ")
    check_data = Helper.search(daftar_kontak,search)
    if check_data == False:
        print("tidak ada data")

def menu_delete_kontak():
    value_delete = input("masukkan pencarian : ")

    if Helper.search(daftar_kontak,value_delete):
        input_choose = Helper.inputYesNo("anda yakin ingin menghapus data yang tampil")
        if Helper.checkYN(input_choose):
            Helper.delete_data_by_input(daftar_kontak,value_delete)
            print("berhasil menghapus data")
        else :
            print("gagal menghapus data")
    else :
        print("tidak ada data")

while(input_menu!=5):
    Helper.printMenuEmprovement()
    input_menu = Helper.inputInteger("Pilih Menu : ",1,5)

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
        menu_cari_kontak()
        input("tekan [enter] jika sudah selesai")
    elif input_menu==4:
        Helper.printClean()
        menu_delete_kontak()
        input("tekan [enter] jika sudah selesai")
    elif input_menu==5:
        Helper.printClean()
        Helper.printClosing()
    else :
        print("Menu tidak tersedia")

