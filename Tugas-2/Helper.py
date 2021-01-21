import re

def inputInteger(message,min,max):
  while True:
    try:
      userInput = int(input(message))
      if userInput<min:
         print("inputan minimal {}".format(min))
         continue
      elif userInput>max:
         print("inputan maximal {}".format(max))
         continue
    except ValueError:
       print("inputan harus Integer, coba lagi")
       continue
    else:
       return userInput 
       break 

def inputTelp(message):
  while True:
    try:
      userInput = input(message)
      if userInput.isdigit()==False:
         print("inputan harus angka")
         continue
      elif len(userInput)<10 or len(userInput)>12:
         print("panjang inputan harus antara 10 sampai 12")
         continue
      elif userInput[0:2] !='08':
         print("nomor telphone harus diawali [08....]")
         continue
    except ValueError:
       print("inputan harus Integer, coba lagi")
       continue
    else:
       return userInput 
       break 


def printMenu():
   printClean()
   print("--- Menu ---")
   print("1. Daftar Kontak")
   print("2. Tambah Kontak")
   print("3. Keluar")

def printMenuEmprovement():
   printClean()
   print("--- Menu ---")
   print("1. Daftar Kontak")
   print("2. Tambah Kontak")
   print("3. Cari Kontak")
   print("4. Delete Kontak")
   print("5. Keluar")


def printClosing():
   print("Program selesai, sampai jumpa!")

def printClean():
   for i in range(0,30):
      print("\n")

#menu1
def menu_daftar_kontak(*daftar_kontak):
   print("daftar_kontak")
   print("=====================")
   if not daftar_kontak :
      print("==data masih kosong==")
      print("")
   else :
      for data in daftar_kontak:
         print_dictionary(**data)
         print("\n")


def print_dictionary(**data_dictionary):
   for key,value in data_dictionary.items():
      print(key,value,sep=" : ")

#menu2 
def add_list_dictionary(list_dictionary,**new_data):
   printClean()
   if(check_new_data(list_dictionary,**new_data)):
      list_dictionary.append(new_data)
      print("kontak sudah berhasil di tambahkan")
      return True
   else :
      menu_daftar_kontak(*list_dictionary)
      print("data yang anda masukkan")
      print_dictionary(**new_data)
      print("data ini sudah ada sebelumnya")
      return False

#pengecheckan data baru
def check_new_data(list_dictionary,**new_data):
   for list_item in list_dictionary:
      for key,value in new_data.items():
         if list_item[key] ==value : 
            return False
   return True

#pencarian data  
def search(list_dictionary,value_search):
   is_have_data = False
   print("hasil data pencarian : ")
   for list_item in list_dictionary:
      is_item = False
      for key,value in list_item.items():
         if re.search(value_search,value):
            is_item = True
            is_have_data =True
      if is_item:
         print_dictionary(**list_item)
   return is_have_data


def inputYesNo(message):
  while True:
    try:
      userInput = input(message+"[Y/N] : ")

    except ValueError:
       print("inputan harus angka, coba lagi")
       continue
    else:
        if userInput=='Y' or userInput == 'N':
            return userInput
            break 

def checkYN(value):
    if value == 'Y':
        return True
    else:
        return False

def delete_data_by_input(list_dictionary,value_search):
   for list_item in list_dictionary:
      is_item = False
      for key,value in list_item.items():
         if re.search(value_search,value):
            is_item =True
      if is_item:
         list_dictionary.remove(list_item)
