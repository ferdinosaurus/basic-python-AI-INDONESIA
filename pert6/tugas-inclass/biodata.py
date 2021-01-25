
class biodata:
    def __init__(self,nama,umur,notelp,alamat):
        self.nama = nama
        self.umur = umur
        self.notelp = notelp
        self.alamat = alamat
        
    def printData(self):
        print("nama {}".format(self.nama))
        print("umur {}".format(self.umur))
        print("notelp {}".format(self.notelp))
        print("alamat {}".format(self.alamat))
        