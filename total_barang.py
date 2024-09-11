def total_barang(barang):
    total = 0
    print("Nama\tJumlah\tHarga")
    for item in barang:
        print(item)
        total += item.subtotal
    print(f"Total pembelian: {total}")