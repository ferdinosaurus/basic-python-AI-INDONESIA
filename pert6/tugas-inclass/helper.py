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
