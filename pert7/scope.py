a = 4
b = 5

def scope():
    global nama, umur
    nama = "Budi"
    umur = 35
    # a = a + b
    # b = a - b
    print(a + b)

scope()
print(nama, umur, sep=', ')