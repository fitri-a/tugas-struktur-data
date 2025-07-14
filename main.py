"""program membuat fungsi CRUD (create,read,upload,delete) 
dalam studi kasus sistem pengelolaan buku"""

import csv #memanggil file csv

buku = []
riwayat_stack = []  # Stack untuk menyimpan riwayat edit/hapus

def load_data(): # untuk memuat data 
    try:
        with open('tambah_buku.csv', mode='r', newline='', encoding='utf-8') as file: #mengelola file tambah_buku.csv
            reader = csv.reader(file)
            for row in reader:
                buku.append(row[0])
    except FileNotFoundError:
        pass

def simpan_data():# untuk menyimpan data yang sudah di kerjakan oleh fungsi load data              
    with open('tambah_buku.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for judul in buku:
            writer.writerow([judul])

def menambahkan():
    judul = input("Masukkan judul buku: ")
    buku.append(judul)
    print("\nBuku berhasil ditambahkan\n")
    simpan_data()

def menampilkan():
    if len(buku) == 0:
        print("\nData masih kosong\n")
    else:
        print("\n== Daftar Buku ==")
        for index, book in enumerate(buku):
            print(f"{index}. {book}")
        print()

def mengedit():
    try:
        index = int(input("Masukkan index: "))
        judul_lama = buku[index]
        judul_baru = input("Masukkan judul baru: ")
        buku[index] = judul_baru
        riwayat_stack.append(("edit", index, judul_lama))  # Simpan ke stack
        print(f"{judul_lama} telah diganti menjadi {judul_baru}\n")
        simpan_data()
    except:
        print("Index tidak valid.\n")

def menghapus():
    try:
        index = int(input("Masukkan index: "))
        judul = buku[index]
        riwayat_stack.append(("hapus", index, judul))  # Simpan ke stack
        del buku[index]
        print(f"{judul} telah dihapus\n")
        simpan_data()
    except:
        print("Index tidak valid.\n")

def lihat_riwayat_stack():
    if not riwayat_stack:
        print("\nTidak ada riwayat perubahan.\n")
    else:
        print("\n== Riwayat (Stack) ==")
        for i, aksi in enumerate(reversed(riwayat_stack)):
            jenis, idx, data = aksi
            print(f"{i+1}. {jenis.upper()} - Index: {idx}, Data: {data}")
        print()

def unduh_stack():
    if not riwayat_stack:
        print("\nTidak ada aksi yang bisa dibatalkan.\n")
        return

    aksi = riwayat_stack.pop()
    jenis, index, data = aksi

    if jenis == "edit":
        buku[index] = data
        print(f"Edit dibatalkan. Judul dikembalikan ke '{data}'\n")
    elif jenis == "hapus":
        buku.insert(index, data)
        print(f"Penghapusan dibatalkan. Buku '{data}' dikembalikan ke index {index}\n")

    simpan_data()

def menu():
    print("==== MENU ====")
    print("[1] Menampilkan data")
    print("[2] Menambahkan data")
    print("[3] Mengedit data")
    print("[4] Menghapus data")
    print("[5] Lihat riwayat (Stack)")
    print("[6] Unduh perubahan terakhir")
    print("[0] Keluar")

    kode = input("Masukkan kode: ")
    print()

    if kode == "1":
        menampilkan()
    elif kode == "2":
        menambahkan()
    elif kode == "3":
        mengedit()
    elif kode == "4":
        menghapus()
    elif kode == "5":
        lihat_riwayat_stack()
    elif kode == "6":
        unduh_stack()
    elif kode == "0":
        print("Program selesai.")
        exit()
    else:
        print("Kode salah.\n")

# Main Loop
load_data()
while True:
    menu()
