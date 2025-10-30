saldo = 1000000

while True:
    print("\nSaldo saat ini: Rp", saldo)
    print("1. Tarik Uang")
    print("2. Keluar")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        tarik = int(input("Masukkan jumlah penarikan: "))
        if tarik > saldo:
            print("Saldo tidak cukup!")
        else:
            saldo -= tarik
            print("Penarikan berhasil!")
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid!")