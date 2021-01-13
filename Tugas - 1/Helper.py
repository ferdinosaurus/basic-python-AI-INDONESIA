import math

math.inf

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

def inputFloat(message,min,max):
  while True:
    try:
      userInput = float(input(message))
      if userInput<min:
         print("inputan minimal {}".format(min))
         continue
      elif userInput>max:
         print("inputan maximal {}".format(max))
         continue
    except ValueError:
       print("inputan harus Integer/Float, coba lagi")
       continue
    else:
       return userInput 
       break 

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

def luas_lingkaran(jari_jari):
    return math.pi*jari_jari**2

def printClosing():
    print("selesai")
    print("terima kasih sudah menggunakan aplikasi ini")