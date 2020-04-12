# Arsip Surat
Merupakan aplikasi desktop sederhana untuk mempermudah pengelolaan surat masuk dan surat keluar menjadi lebih efektif dan efisien.

## Yang harus ter install di komputer anda :
-	[x] Python 2.7 (https://www.python.org/downloads/)
-	[x] Apache Cassandra (https://medium.com/@sushantgautam_930/simple-way-to-install-cassandra-in-windows-10-6497e93989e6)
-	[x] Cassandra Driver dengan mengetikkan ‘pip install cassandra driver’ pada CMD
-	[x] GUI toolkit : Tkinter

## Cara menjalankan aplikasi :
1. Clone/download repository ini
2. Jalankan Cassandra Server sebagai ‘cassandra.bat -f’ dengan CMD run as administrator dari directory bin. Jangan ditutup, biarkan terus berjalan
3. Kemudian, buka CMD lainnya, buka directory tempat penyimpanan Cassandra. Untuk menjalankan cqlsh dengan mengetikkan ‘cqlsh’
4. Buka IDLE (Python GUI)
5. Open project dengan nama file ‘Arsip Surat.py’
6. Run module
7. Hasil run akan menampilkan desktop app Arsip Surat
8. Login sesuai kebutuhan, sebagai Admin ataupun logged in as a User.

## Fitur aplikasi :
**Admin**
-	Login menggunakan username ‘admin’ dan password ‘12345’.
-	Melihat tab menu ‘Home’ yang berisi penjelasan mengenai aplikasi, disertai button untuk melihat jam.
-	Melihat daftar surat masuk dan surat keluar yang telah di input oleh user pada tab menu ‘Surat Masuk’ dan ‘Surat Keluar’.
-	Menghapus daftar surat masuk dan surat keluar yang mungkin terjadi double input oleh user pada tab menu ‘Surat Masuk’ dan ‘Surat Keluar’.
-	Melihat profile pada tab menu ‘Profile’.
-	Button keluar yang ada disetiap window.

**User**
-	Logged in as a User.
-	Melihat tab menu ‘Home’ yang berisi penjelasan mengenai aplikasi, disertai button untuk melihat jam.
-	Menginput surat masuk atau surat keluar pada tab menu ‘Surat Masuk’ dan ‘Surat Keluar’.
-	Melihat profile pada tab menu ‘Profile’.
-	Button keluar yang ada disetiap window.

## Video menjalankan aplikasi :
Klik link berikut >> [Video Arsip Surat](https://youtu.be/2prKjj5r-js)
atau https://youtu.be/2prKjj5r-js (video run module python dimulai pada 1:45)
