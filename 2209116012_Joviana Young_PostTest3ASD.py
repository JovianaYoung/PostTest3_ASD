import os
os.system('cls')

# Membuat class untuk node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Membuat class untuk linked list
class LinkdList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Menambah node baru
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            saat_ini = self.head
            while saat_ini.next is not None:
                saat_ini = saat_ini.next
            saat_ini.next = new_node
        self.size += 1
        
    # Menghapus node
    def delete(self, data):
        if not self.head:
            print()
            print(">>> Nomor Plat Motor Tidak Tersedia/Belum di inputkan <<<")
            print("----------------------------------------------------------")
            return
        if self.head.data == data:
            print()
            print("  >>> Karcis Parkir Telah Berhasil di Hapus <<<")
            print("-------------------------------------------------")
            self.head = self.head.next
            return
        saat_ini = self.head
        while saat_ini.next:
            if saat_ini.next.data == data:
                saat_ini.next = saat_ini.next.next
                return
            saat_ini = saat_ini.next
        print()
        print(">>> Nomor Plat Motor Tidak Tersedia/Belum di Inputkan <<<")
        print("----------------------------------------------------------")

    # Melihat keseluruhan isi antrian
    def read(self):
        if self.head is None:
            print()
            print("     >>> Antrian Parkir Kosong <<< ")
            return
        saat_ini = self.head
        while saat_ini is not None:
            print(saat_ini.data)
            saat_ini = saat_ini.next

    # menampilkan nomor plat sepeda motor yang sedang parkir
    def show(self):
        print("----------------------------------------")
        print("Nomor Plat Motor yang Masih Terparkir: ")
        self.read()
        print("----------------------------------------")

# Tampilan Menu Aplikasi
def display():
    linked_list = LinkdList()
    while True:
        print("|=================================================|")
        print("|         Menu Aplikasi Karcis Parkir Motor       |")
        print("|=================================================|")
        print("| 1. Menambahkan Nomor Antrian karcis Motor       |")
        print("| 2. Menghapus Nomor Antrian karcis Motor         |")
        print("| 3. Menampilkan Nomor Plat Motor yang Terparkir  |")
        print("| 4. Keluar dari Program Aplikasi                 |")
        print("==================================================|")
        choice = int(input("Masukkan pilihan Anda (1-4): "))
        if choice == 1:
            os.system('cls')
            data = input("Inputan Nomor Plat Motor: ")
            linked_list.insert(data)
            print("-----------------------------------------")
            print(">>> Karcis Telah Berhasil Ditambahkan <<<")
            print()
            ulang = "y"
            if ulang == "y":
                ulang = input("Apakah Anda Ingin Kembali ke Menu y/t : ")
                os.system('cls')
                if ulang == "y":
                    display
                elif ulang == "t":
                    print()
                    print(">>> Terima Kasih Telah Menggunakan Aplikasi Kami <<<")
                    print("-----------------------------------------------------")
                    break
                    
        elif choice == 2:
            os.system('cls')
            data = input("Inputkan Nomor Plat Motor yang Ingin Dihapus: ")
            linked_list.delete(data)
            print()
            tambah = "y"
            if tambah == "y":
                tambah = input("Apakah Anda Ingin Kembali ke Menu y/t : ")
                os.system('cls')
                if tambah == "y":
                    display
                elif tambah == "t":
                    print()
                    print("Terima Kasih Telah Menggunakan Aplikasi Kami.")
                    print("---------------------------------------------")
                    break

        elif choice == 3:
            os.system('cls')
            linked_list.show()
            print()
            tambah = "y"
            if tambah == "y":
                tambah = input("Apakah Anda Ingin Kembali ke Menu y/t : ")
                os.system('cls')
                if tambah == "y":
                    display
                elif tambah == "t":
                    print()
                    print("Terima Kasih Telah Menggunakan Aplikasi Kami.")
                    print("---------------------------------------------")
                    break
                
        elif choice == 4:
            os.system('cls')
            print("Terima Kasih Telah Menggunakan Aplikasi Kami.")
            print("----------------------------------------------")
            break

        else:
            print()
            print("Pilihan yang Anda Masukkan Kurang Tepat. Silakan Coba Lagi.")
            print("----------------------------------------------------------")
            tambah = "y"
            if tambah == "y":
                print()
                tambah = input("Apakah Anda Ingin Kembali ke Menu y/t : ")
                os.system('cls')
                if tambah == "y":
                    display
                elif tambah == "t":
                    print()
                    print("Terima Kasih Telah Menggunakan Aplikasi Kami.")
                    print("---------------------------------------------")
                    break

if __name__ == '__main__':
    display()
