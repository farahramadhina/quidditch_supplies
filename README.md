# Tugas 2: Implementasi Model-View-Template (MVT) pada Django #
# Farah Dhiya Ramadhina/PBP B/2206082934 #

## A. Implementasi Checklist *step-by-step* ##
### 1. Membuat sebuah proyek Django baru. ###
* Membuat direktori baru dengan nama 'quidditch_supplies' pada folder PBP Farah di Desktop, yang saya gunakan untuk menyimpan semua file PBP saya pada semester ini.
* Membuat virtual environment pada terminal direktori yang baru saya buat dengan menjalankan prompt berikut : 'python -m venv env'
* Mengaktifkan virtual environment dengan prompt berikut : 'source env/bin/activate' Virtual environment akan aktif dan dapat terlihat dengan adanya (env) di awal baris input terminal
* Membuat berkas requirements.txt pada direktori yang baru kita buat, dan mengisi berkas tersebut dengan beberapa dependencies. Dependencies merupakan komponen atau modul yang diperlukan oleh suatu perangkat lunak untuk berfungsi, termasuk library, framework, atau package. 
* Menjalankan virtual environment, lalu memasang dependencies dengan menginput prompt berikut pada terminal : 'pip install -r requirements.txt'
* Membuat proyek Django bernama quidditch_supplies dengan prompt : 'django-admin startproject quidditch_supplies .'
* Buka settings.py yg ada di direktori yang telah saya buat, lalu menambahkan "*" pada ALLOWED_HOSTS menjadi
'ALLOWED_HOSTS = ["*"]'. Dengan menetapkan nilai ["*"], akan memungkinkan aplikasi saya diakses secara luas. 
* Memastikan bahwa berkas 'manage.py' ada pada direktori yang aktif pada shell saya saat ini, lalu jalankan server Django dengan prompt berikut : './manage.py runserver' 
* Buka 'http://localhost:8000/' pada browser untuk memastikan bahwa aplikasi Django saya berhasil dibuat (ditandai dengan adanya animasi roket dan teks yang bertuliskan installation succesful pada halaman yang dibuka)
* Aplikasi Django selesai dibuat. Tekan 'Control+C' pada shell untuk menghentikan server, dan menonaktifkan virtual environment dengan prompt : 'deactivate'

### 2. Membuat aplikasi dengan nama 'main' pada proyek tersebut. ###
* Buka terminal pada direktori utama quidditch_supplies, lalu aktifkan virtual environment yang telah dibuat sebelumnya dengan menjalankan prompt berikut : 'source env/bin/activate'
* Jalankan prompt berikut untuk membuat aplikasi baru bernama main : 'python manage.py startapp main' 
* Buka berkas settings.py pada direktori proyek quidditch_supplies, lalu tambahkan 'main' pada daftar aplikasi yg ada pada variabel 'INSTALLED_APPS' untuk mendaftarkan aplikasi 'main' ke dalam proyek.

### 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main. ###

### 4. Membuat model pada aplikasi 'main' dengan nama 'Item' dan memiliki atribut wajib sebagai berikut : 
'name' sebagai nama item dengan tipe 'CharField'.
'amount' sebagai jumlah item dengan tipe 'IntegerField'.
'description' sebagai deskripsi item dengan tipe 'TextField'. ### 
* Buka berkas 'models.py' pada direktori aplikasi 'main'
* Isi berkas 'models.py' dengan menambahkan atribut wajib dan pilihan sesuai yang kita inginkan seperti berikut : 
'from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()'

### 5. Membuat sebuah fungsi pada 'views.py' untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. ###
* Buka berkas 'views.py' pada berkas aplikasi 'main', lalu impor modul yg dibutuhkan untuk membuat fungsi 'show_main' seperti berikut : 
'from django.shortcuts import render'
* Tambahkan fungsi 'show_main' di bawah baris impor yang akan dikembalikan dalam template HTML yang menampilkan nama dan kelas saya seperti berikut : 
'def show_main(request):
    context = {
        'name': 'Farah Dhiya Ramadhina',
        'class': 'PBP B'
    }
    return render(request, "main.html", context)'

### 6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. ###
* 

### 7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. ###
* Buka Adaptable.io pada browser, login menggunakan GitHub, lalu tekan tombol 'New App'.
* Pilih 'Connect an Existing Repository', dan pilih repositori proyek 'quidditch_supplies' yang telah saya buat sebagai basis aplikasi yang akan di-deploy. Pilih branch 'main' sebagai *deployment branch*.
* Pilih 'Python App Template' sebagai *template deployment* dan 'PostgreSQL' sebagai tipe basis data yang akan digunakan.
* Sesuaikan versi Python dengan spesifikasi python saya yaitu '3.11' dan pada bagian 'Start Command' masukkan prompt 'python manage.py migrate && gunicorn quidditch_supplies.wsgi.'
* Masukkan nama aplikasi yang akan menjadi nama domain situs web aplikasi, lalu centang bagian 'HTTP Listener on PORT' dan klik 'Deploy App' untuk memulai proses deployment aplikasi.


## B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. ##
***


## C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? ##
Virtual environment digunakan dalam membuat aplikasi web berbasis Django untuk menjaga kerapihan dan mengisolasi pengembangan perangkat lunak. 

1. **Isolasi Paket dan Dependencies**
Virtual environment memungkinkan kita untuk membuat lingkungan terisolasi di mana kita dapat menginstal dan mengelola dependencies secara independen untuk setiap proyek. Hal ini untuk mencegah konflik jika kita memiliki beberapa proyek yang berbagi dependencies yang sama dengan versi paket yang berbeda.

2. **Mempermudah Pengelolaan Paket**
Dengan virtual environment, kita dapat menggunakan pip (Python package manager) untuk dengan mudah menginstal, menghapus, dan mengelola paket Python yang diperlukan untuk proyek tertentu tanpa mempengaruhi paket-paket di luar lingkungan tersebut.

3. **Menghindari Masalah Kompatibilitas**
Dengan virtual environment, kita memastikan bahwa versi paket yang kita gunakan cocok satu sama lain, sehingga mengurangi kemungkinan terjadinya *compatibility issues*.

4. **Kemudahan Berbagi**
Virtual environment membuat proyek kita lebih mudah dipindahkan ke tempat lain atau dibagikan dengan tim tanpa perlu khawatir tentang masalah *dependencies*.

Kita sebenarnya bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi hal ini berisiko, karena tanpa virtual environment, paket Python akan diinstal secara global di komputer kita. Hal ini bisa menyebabkan masalah jika kita bekerja pada beberapa proyek yang menggunakan versi paket yang berbeda. Oleh karena itu, lebih baik menggunakan virtual environment dalam pengembangan Django dan Python agar proyek kita lebih rapi dan terhindar dari masalah.

## D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. ##
***