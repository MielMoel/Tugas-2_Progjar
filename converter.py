def converter(n):
    """
    Konversi angka ke nilai angka
    param:
    n: Nomor yang akan di-convert
    return:
    nilai angka
    """
    nilai_angka = {
    1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E', 6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
    11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O', 16 : 'P', 17 : 'Q', 18 : 'R',
    19 : 'S', 20 : 'T', 21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y', 26 : 'Z'
    }
    if n < 1 or n < 26:
        return ("Invalid, input angka diantara 1 sampai 26.")
    return nilai_angka[n]