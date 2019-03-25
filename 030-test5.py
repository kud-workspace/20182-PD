#!/usr/bin/env python3

# input/output
def kalkulasi_operasi(a, b, c):
    setengah = 0.5 # luas segitiga = 1/2 luas segi empat
    persegi = a * b # operasi pertama
    segitiga = b * c * 0.5 # operasi kedua
    hasil = c * a + b # operasi ketiga

    print("Kalau a adalah panjang dan b adalah lebar maka luas persegi yaitu %d x %d = %d" %(a, b, persegi))
    print("Kalau b adalah panjang dan c adalah tinggi maka segitiga yaitu %d x %d x %1.1f = %d" %(b, c, setengah, segitiga))
    print("a=%d b=%d c=%d maka (c x a) + b= (%d x %d) + %d = %d" %(a, b, c, c, a, b, hasil))

# kondisional if
def bayar_tujuan(kota, harga, tiket, tujuan, bayar):
    print("Total Bayar Tujuan %s adalah" %(kota))
    jumlah = tiket * harga # harga normal

    if bayar == 1: # Reguler
        print("Tiket Reguler ->", "%d x %d = %d" %(tiket, harga, jumlah))

    elif bayar == 2: # Diskon 10%
        print("Tiket Promo ->", "(%d x %d)-(%d x %d x 0.1) = %d" %(tiket, harga, tiket, harga, proses_diskon(jumlah)))

    elif bayar == 3: # Tuslah 5%
        print("Tiket Hari Besar ->", "(%d x %d)+(%d x %d x 0.05) = %d" %(tiket, harga, tiket, harga, proses_tuslah(jumlah)))

# bilangan berulang
def harga_tiket(kota, harga):
    print("TIKET TUJUAN %s" %(kota))
    print("Jumlah	  Reguler	Promo		Hari Besar")
    for tiket in range(1, 11): # 1 - 10
        jumlah = tiket * harga

        print(" %d	%d		 %d		    %d" %(tiket, jumlah, proses_diskon(jumlah), proses_tuslah(jumlah)))

# fungsi unified
def proses_info(tujuan, tiket, bayar):
    if tujuan == 1: # Jakarta
        kota = 'JAKARTA'
        harga = 1500

    elif tujuan == 2: # Surabaya
        kota = 'SURABAYA'
        harga = 2000

    elif tujuan == 3: # Bandung
        kota = 'BANDUNG'
        harga = 2500

    if pilihan == 2: # kalkulasi harga tiket
        return bayar_tujuan(kota, harga, tiket, tujuan, bayar)
    else: # daftar harga tiket
        return harga_tiket(kota, harga)

# operasi dengan diskon
def proses_diskon(jumlah):
    return jumlah - jumlah * 0.1 # 10%

# operasi dengan tuslah
def proses_tuslah(jumlah):
    return jumlah + jumlah * 0.05 # 5%

print("""Menu
1. Input Output
2. Kondisional IF
3. Bilangan berulang (GUNAKAN FOR)
4. Display  loop dalam loop (GUNAKAN DO WHILE)
5. Keluar""")
pilihan = int(input("Masukan pilihan anda "))

if pilihan == 1: # input/output
    a = int(input("Masukan Nilai a "))
    b = int(input("Masukan Nilai b "))
    c = int(input("Masukan Nilai c "))

    kalkulasi_operasi(a, b, c)

elif pilihan == 2: # kondisional if
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

elif pilihan == 3: # bilangan berulang
    tujuan = int(input("Masukan Kode Tujuan	: "))

    proses_info(tujuan, 0, 0) # parameter 2 dan 3 tidak terpakai

elif pilihan == 4: # loop dalam loop
    raise Exception("Opsi %d belum diimplementasikan" %(pilihan))

elif pilihan == 5: # keluar aplikasi
    quit()

else: # invalid
    raise ValueError("Opsi %d adalah tidak valid" %(pilihan))
