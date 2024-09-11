# items.py (module)
class barang:
    def __init__(self, nama, harga, kuantitas):
        """"
        args : self
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas
        self.subtotal = harga * kuantitas

    def __str__(self):
        return f"{self.nama}\t{self.kuantitas}\t{self.subtotal}"