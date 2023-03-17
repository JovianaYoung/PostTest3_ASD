## Biodata Penulis
Nama: Joviana Young
NIM : 2209116012
Prodi : Sistem Informasi A-22

# POSTTEST3 ASD

# Aplikasi Karcis Parkir Motor
Aplikasi Karcis parkir Motor ini merupakan aplikasi pendataan yang terdiri dari tambah data, hapus data, tampilan data dan keluar program.

## A. Features Aplikasi Karcis Parkir Motor

- Menambahkan nomor antrian karcis motor.
- Menghapus nomor antrian karcis motor.
- Menampilkan nomor plat motor yang. terparkir.
- Keluar dari program aplikasi.

## B. Cara Kerja Program
Pada program ini saya menggunakan single linked list dengan tema antrian karcis motor menggunakan konsep dasar linked list, yaitu menghubungkan satu node dengan node lainnya melalui pointer. Pada program ini, setiap node merepresentasikan satu kendaraan yang masuk ke dalam antrian karcis motor.

## C. Fungsionalitas Program
Program ini berfungsi untuk mendata dengan menambahkan nomor antrian karcis setiap terdapat motor yang ingin masuk kedalam parkiran. Jika motor tersebut ingin keluar dari parkiran maka data nomor antrian akan dihapus agar penjaga mengetahui bahwa kendaraan tersebut sudah tidak terparkir di dalam area parkiran motor. Program ini juga dapat menampilkan nomor plat motor yang masih terparkir didalam area parkiran agar memudahkan petugas parkir dalam mengetahui berapakah motor yang masih terparkir didalam area parkiran. Sehingga dengan adanya program ini dapat memudahkan petugas parkir dalam menjalankan pekerjaannya.

## D. Cara Kerja Aplikasi
Aplikasi ini bekerja dengan mendata plat motor yang masuk lalu datanya akan disimpan, jika motor tersebut ingin keluar dari area parkiran maka data dari motor tersebut akan dihapus yang dimana dapat dijadikan sebagai bukti bahwa kendaraan tersebut sudah tidak terparkir di dalam area parkir jika terjadi sebuah hal yang tidak diinginkan, aplikasi juga dapat menampilkan nomor plat motor yang masih terparkir didalam area parkir.

## E. Output Program
Output dari program ini akan menampilkan tampilan menu aplikasi karcis parkir motor yang dimana didalam menu tersebut terdapat 4 atribut sebagai berikut:
1.	menambahkan nomor antrian karcis motor, 
2.	menghapus nomor antrian karcis motor,
3.	menampilkan nomor plat motor yang terparkir, dan
4.	keluar dari program aplikasi.

- Jika pilihan adalah 1 maka user akan diminta untuk menginputkan nomor plat motor yang ingin masuk kedalam area parkiran, jika nomor plat motor sudah di inputkan maka akan muncul tampilan “Karcis parkir Telah Berhasil Ditambahkan” yang artinya nomor plat motor tersebut telah terdata didalam aplikasi karcis parkir motor dan dapat masuk kedalam area parkir. Jika semua proses telah berhasil maka ada ada pertanyaan “Apakah Anda Ingin Kembali ke Menu y/t” jika pilihan = “y” maka akan memunculkan tampilan menu aplikasi, jika pilihhan = “t” maka akan secara otomatis keluar dari program aplikasi.

- Jika pilihan adalah 2 maka user akan diminta untuk menginputkan data nomor plat motor yang ingin di hapus dalam area parkiran, jika nomor plat motor sudah di inputkan maka akan muncul tampilan “Karcis parkir Telah Berhasil di Hapus” yang artinya nomor plat motor tersebut telah terhapus dari dalam aplikasi karcis parkir. Dan, jika user menginputkan data yang belum di inputkan maka akan muncul tampilan “Nomor Plat Motor Tidak Tersedia/Belum di Inputkan” yang artinya nomor plat tersebut tidak ada didalam aplikasi karcis parkir atau data tersebut belum di inputkan. Jika semua proses telah berhasil maka ada ada pertanyaan “Apakah Anda Ingin Kembali ke Menu y/t” jika pilihan = “y” maka akan memunculkan tampilan menu aplikasi, jika pilihhan = “t” maka akan secara otomatis keluar dari program aplikasi.

- Jika pilihan adalah 3 maka akan menampilkan tampilan "nomor plat motor yang yang masih terparkir" dan jika parkiran tersebut kosong maka akan muncul tampilan “Antrian Parkir Kosong”. Jika semua proses telah berhasil maka ada ada pertanyaan “Apakah Anda Ingin Kembali ke Menu y/t” jika pilihan = “y” maka akan memunculkan tampilan menu aplikasi, jika pilihhan = “t” maka akan secara otomatis keluar dari program aplikasi.

- Jika pilihan adalah 4 maka akan menampilkan tampilan “Terima Kasih Telah Menggunkan Aplikasi Kami.” Yang berarti telah keluar dari aplikasi.

## F. Penjelasan Elemen yang digunakan Pada Program
•	Class Node adalah sebuah class untuk merepresentasikan node dalam linked list. Setiap node memiliki dua atribut yaitu data untuk menyimpan data kendaraan, dan next untuk menyimpan pointer ke node berikutnya.

•	Class LnkdList adalah sebuah class untuk merepresentasikan linked list. Setiap linked list memiliki sebuah atribut yaitu head untuk menyimpan node pertama (head node).

•	Def insert adalah sebuah method untuk menambahkan node baru ke dalam linked list. Method ini menerima sebuah parameter data yang berisi data kendaraan. Pertama-tama, method ini membuat sebuah node baru dengan data yang diberikan. Jika linked list masih kosong (tidak memiliki head node), maka node baru tersebut akan menjadi head node. Jika tidak, maka method ini akan mencari node terakhir dalam linked list, kemudian menghubungkannya dengan node baru.

•	Def delete adalah sebuah method untuk menghapus node pertama (head node) dari linked list dan mengembalikan data kendaraan yang terdapat pada node tersebut. Jika linked list masih kosong, maka method ini akan mengembalikan nilai None.

•	Def read adalah sebuah method untuk mencetak semua data kendaraan yang terdapat dalam linked list, dimulai dari head node dan berakhir pada node terakhir.

•	Def show adalah sebuah method untuk menampilkan nomor plat motor yang masih terparkir.

•	Def display adalah sebuah method yang digunakan untuk menampilkan semua elemen yang terdapat pada linked list secara berurutan, dimulai dari elemen pertama hingga elemen terakhir. Fungsi ini biasanya digunakan untuk memeriksa isi linked list dan memastikan bahwa setiap elemen terhubung dengan benar.
