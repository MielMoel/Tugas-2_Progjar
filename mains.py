import items
import calculator

def mains():
    items_list = []
    while True:
        nama = input("Nama Barang: ")
        harga = int(input("Harga: "))
        kuantitas = int(input("Jumlah: "))
        item = barang.Item(nama, harga, kuantitas)
        barang_list.append(item)
        cont = input("Tambah barang? (y/n): ")
        if cont.lower() != 'y':
            break
    calculator.total_barang(barang_list)

if __name__ == "__mains__":
    mains()