#!/usr/bin/env python3

def put(a, b, c):
    setengah = 0.5

    print("Kalau a adalah panjang dan b adalah lebar maka luas persegi yaitu %d x %d = %d" %(a, b, a * b))
    print("Kalau b adalah panjang dan c adalah tinggi maka segitiga yaitu %d x %d x %1.1f = %d" %(b, c, setengah, b * c * setengah))
    print("a=%d b=%d c=%d maka (c x a) + b= (%d x %d) + %d = %d" %(a, b, c, c, a, b, c * a + b))

def kondisional_if(kota, harga, tiket, tujuan, bayar):
    print("Total Bayar Tujuan %s adalah" %(kota))
    if bayar == 1:
        print("Tiket Reguler ->", "%d x %d = %d" %(tiket, harga, tiket * harga))
    elif bayar == 2:
        print("Tiket Promo ->", "(%d x %d)-(%d x %d x 0.1) = %d" %(tiket, harga, tiket, harga, tiket * harga - tiket * harga * 0.1))
    elif bayar == 3:
        print("Tiket Hari Besar ->", "(%d x %d)+(%d x %d x 0.05) = %d" %(tiket, harga, tiket, harga, tiket * harga + tiket * harga * 0.05))

def berulang(kota, harga):
    print("TIKET TUJUAN %s" %(kota))
    print("Jumlah	  Reguler	Promo		Hari Besar")
    for jumlah in range(1, 11):
        print(" %d	%d		 %d		    %d" %(jumlah, jumlah * harga, jumlah * harga - jumlah * harga * 0.1, jumlah * harga + jumlah * harga * 0.05))

def proses_info(tujuan, tiket, bayar):
    if tujuan == 1:
        kota = 'JAKARTA'
        harga = 1500

    elif tujuan == 2:
        kota = 'SURABAYA'
        harga = 2000

    elif tujuan == 3:
        kota = 'BANDUNG'
        harga = 2500

    if pilihan == 2:
        return kondisional_if(kota, harga, tiket, tujuan, bayar)
    else:
        return berulang(kota, harga)

print("""Menu
1. Input Output
2. Kondisional IF
3. Bilangan berulang (GUNAKAN FOR)
4. Display  loop dalam loop (GUNAKAN DO WHILE)
5. Keluar""")
pilihan = int(input("Masukan pilihan anda "))

if pilihan == 1:
    a = int(input("Masukan Nilai a "))
    b = int(input("Masukan Nilai b "))
    c = int(input("Masukan Nilai c "))

    put(a, b, c)

if pilihan == 2:
    print("""KETERANGAN PEMBELIAN TIKET
KODE TUJUAN -> 1. JAKARTA    Harga Rp. 1.500 dlm ribuan
               2. SURABAYA   Harga Rp. 2.000 dlm ribuan
               3. BANDUNG    Harga Rp. 2.500 dlm ribuan
KODE BAYAR  -> 1. REGULER    -> Harga Normal
               2. PROMO      -> Potongan 10 %
               3. HARI BESAR -> Tuslah Naik 5 %""")
    tiket = int(input("Jumlah Tiket Penumpang	: "))
    tujuan = int(input("Masukan Kode Tujuan	: "))
    bayar = int(input("Masukan Kode Bayar	: "))

    proses_info(tujuan, tiket, bayar)

elif pilihan == 3:
    tujuan = int(input("Masukan Kode Tujuan	: "))

    proses_info(tujuan, 0, 0)

elif pilihan == 4:
    raise Exception("Opsi %d belum diimplementasikan" %(pilihan))

elif pilihan == 5:
    quit()

else:
    raise ValueError("Opsi %d adalah tidak valid" %(pilihan))
