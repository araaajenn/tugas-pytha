# Fungsi login
def login():
    while True:
        nama = input("Masukan nama Anda : ")
        nim = input("Masukan NIM Anda : ")

        if nama == "Aura Syahrawani Nasir" and nim == "2309116047":
            return True
        else:
            print("Login gagal maz, ulang dong")
    
# Manggil Function(def) login, buat apa? buat login lah
if login():
    print("Berhasil Login maz!")

    #Nampilin menu dong
    print("Pilih sisi yang mau Kamu hitung : ")
    print("1. Alas")
    print("2. Sisi Tegak")
    print("3. Sisi Miring")

    pilihan = input("Masukan nomor pilihan Anda (1, 2 atau 3) : ")

    # Mulai hitung sisi sesuai pilihan
    if pilihan == "1":
        sisi_tegak = float(input("Masukan Panjang sisi tegak : "))
        sisi_miring = float(input("Masukan Panjang sisi miring : "))
        alas = (sisi_miring**2 - sisi_tegak**2)**0.5
        print("Panjang alas adalah : ", alas)
    
    elif pilihan == "2":
        alas = float(input("Masukan Panjang alas : "))
        sisi_miring = float(input("Masukan Panjang sisi miring : "))
        sisi_tegak = (sisi_miring**2 - alas**2)**0.5
        print("Panjang Sisi Tegak adalah : ", sisi_tegak)
    
    elif pilihan == "3":
        alas = float(input("Masukan Panjang alas : "))
        sisi_tegak = float(input("Masukan Panjang sisi tegak : "))
        sisi_miring = (alas**2 + sisi_tegak**2)**0.5
        print("Panjang Sisi Miring adalah : ", sisi_miring)
    else:
        print("Cuma boleh isi 1, 2, atau 3. Sisanya tidak Valid maz")
    
else: 
    print("Anda tidak ada akses ke program ini")