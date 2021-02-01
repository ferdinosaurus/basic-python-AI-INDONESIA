def angka(x):
    def call():
        print(x)
    return call

output = angka("Halo World")
output()