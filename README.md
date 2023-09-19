# Tugas 3 : Implementasi Form dan Data Delivery pada Django #
## Farah Dhiya Ramadhina/PBP B/2206082934 ##

## A. Apa perbedaan antara form `POST` dan form `GET` dalam Django? ##
### `POST` ###
Dengan metode `POST` pada Django, data formulir dikirimkan dalam badan permintaan HTTP. Di mana data, seperti nilai variabel tidak ditampilkan di URL, sehingga lebih aman untuk mengirim data-data sensitif seperti *password*. POST digunakan untuk mengirim data yang akan dimasukkan atau diperbarui di server, seperti saat menambahkan entri pada database. Input data dalam metode POST pada Django dilakukan dengan melalui form.
### `GET` ###
 Dalam metode `GET` pada Django, data formulir dikirimkan sebagai bagian dari URL. Hal ini membuat data, seperti nilai variabel terlihat dan dapat diakses oleh siapa saja yang melihat URL tersebut sehingga dinilai kurang aman. Namun, dengan metode GET, user dapat dengan mudah memasukkan atau mengambil data dari server tanpa memengaruhi data di server. Misalnya, saat kita ingin mencari sesuatu di *search engine*, kita menggunakan metode `GET` karena kita hanya mengambil informasi tanpa mengubahnya. Input data dalam metode POST pada Django dilakukan dengan melalui link.

## B. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? ##
- **XML (eXtensible Markup Language)**
XML adalah format teks yang digunakan untuk mengorganisir dan menyusun data dalam struktur hierarkis. XML sangat fleksibel dan dapat digunakan untuk merepresentasikan berbagai jenis data. Namun, XML cenderung lebih berat dan sulit dibaca oleh manusia karena memiliki banyak tag.
- **JSON (JavaScript Object Notation)**
JSON adalah format data ringan yang mudah dibaca oleh manusia dan mudah diproses oleh mesin. JSON sangat populer dalam pengiriman data antara aplikasi web karena memiliki struktur yang sederhana dengan objek dan daftar. JSON adalah format yang ideal untuk API REST.
- **HTML (Hypertext Markup Language)** 
HTML adalah bahasa markup yang digunakan untuk membuat halaman web. HTML berfokus pada tampilan dan struktur halaman web. HTML tidak digunakan untuk pertukaran data antara aplikasi, tetapi untuk menampilkan konten ke pengguna melalui browser. 

## C. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? ##
- JSON digunakan secara luas karena kemudahan dalam membaca dan menulis data, baik oleh manusia maupun komputer.
- JSON memiliki format yang sederhana dengan struktur objek dan daftar, yang membuatnya ideal untuk merepresentasikan data yang lebih kompleks.
- Banyak bahasa pemrograman memiliki dukungan bawaan untuk mengurai dan menghasilkan JSON, sehingga memudahkan komunikasi antara berbagai teknologi.
- JSON ringan dan efisien dalam penggunaan bandwidth, yang penting dalam pengiriman data melalui jaringan.
- JSON sering digunakan dalam pengembangan aplikasi web berbasis RESTful API, di mana data dikirimkan dan diterima dalam format JSON yang mudah diinterpretasi oleh server dan klien.

## D. Implementasi Checklist *step-by-step*. ##
### Membuat input form untuk menambahkan objek model pada app sebelumnya. ###
* Mengaktifkan virtual environment dengan menjalankan *prompt* berikut pada terminal direktori aplikasi kita `source env/bin/activate` 
* Mengubah routing `main/` menjadi `/` dengan mengubah kode path `main/` menjadi `' '`  pada *file* `urls.py` yang ada pada folder `quidditch_supplies` seperti berikut : 
```ruby
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```
* Menjalankan server dengan perintah `python manage.py runserver` dan buka http://localhost:8000/  untuk melihat hasilnya
* Buat folder `templates` pada *root folder* dan buat file HTML berjudul `base.html` yang berfungsi sebagai *template* dasar untuk menjadi kerangka umum halaman web lainnya. Isi file `base.html` dengan kode berikut : 
```ruby
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
* Buka file `settings.py` pada subdirektori `quidditch_supplies` dan tambahkan kode ini pada baris yg mengandung `TEMPLATES` : 
```ruby
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        ...
    }
```
* Ubah file `main.html` pada subdirektori `templates` yg ada pada `main` seperti berikut : 
```ruby
{% extends 'base.html' %}

{% block content %}
    <h1>Quidditch Supplies Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```
* Buat file dengan nama `forms.py` pada direktori `main` dan isi dengan kode berikut :
```ruby
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "price", "description", "category"] #Pilihan field saya tulis sesuai yang saya inginkan ada pada produk saya
```
* Tambahkan kode berikut pada file `views.py` pada folder `main` :
```ruby
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
dan tambahkan fungsi `create_request` seperti berikut untuk membuat formulir yang dapat menambahkan produk setelah data di-*submit* dari form : 
```ruby
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
* Buka file `views.py` dan ubah fungsi `show_main` menjadi seperti berikut : 
```ruby
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Farah Dhiya Ramadhina', # Nama kamu
        'class': 'PBP B', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
```
* Buka file `urls.py` pada folder `main` dan import fungsi `create_product` serta tambahkan *path url* dalam `urlpatterns` seperti berikut : 
```ruby
from main.views import show_main, create_product
...
path('create-product', create_product, name='create_product'),
```
* Buat file dengan nama `create_product.html` pada direktori `main/templates` dan isi dengan kode berikut : 
```ruby
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
* Tambahkan kode berikut dalam `{% block content %}` pada file `main.html` :
```ruby
...
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Price</th>
        <th>Description</th>
        <th>Category</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.amount}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.category}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

### Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. ###
#### Fungsi Views dalam format XML ####
* Tambahkan kode berikut pada file `views.py` pada folder `main` : 
```ruby
from django.http import HttpResponse
from django.core import serializers
```
* Buat fungsi `show_xml` seperti berikut : 
```ruby
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
#### Fungsi Views dalam format JSON ####
* Buat fungsi `show_json` seperti berikut pada file `views.py` yang ada pada folder `main` : 
```ruby
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
#### Fungsi Views dalam format XML by ID ####
* Buat fungsi `show_xml_by_id` seperti berikut pada file `views.py` yang ada pada folder `main` : 
```ruby
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
#### Fungsi Views dalam format JSON by ID ####
* Buat fungsi `show_json_by_id` seperti berikut pada file `views.py` yang ada pada folder `main` : 
```ruby
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2. ###
#### Routing URL fungsi views dalam format XML ####
* Buka file `urls.py` pada folder `main` dan import fungsi `show_xml` serta tambahkan *path url* dalam `urlpatterns` seperti berikut : 
```ruby
from main.views import show_main, create_product, show_xml
...
path('xml/', show_xml, name='show_xml'), 
...
```
#### Routing URL fungsi views dalam format JSON ####
* Buka file `urls.py` pada folder `main` dan import fungsi `show_json` serta tambahkan *path url* dalam `urlpatterns` seperti berikut : 
```ruby
from main.views import show_main, create_product, show_xml, show_json
...
path('json/', show_json, name='show_json'),
...
```
#### Routing URL fungsi views dalam format XML by ID ####
* Buka file `urls.py` pada folder `main` dan import fungsi `show_xml_by_id` serta tambahkan *path url* dalam `urlpatterns` seperti berikut : 
```ruby
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, 
...
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
...
```
#### Routing URL fungsi views dalam format JSON by ID ####
* Buka file `urls.py` pada folder `main` dan import fungsi `show_json_by_id` serta tambahkan *path url* dalam `urlpatterns` seperti berikut : 
```ruby
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
...
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
...
```

## E. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md.` ##
### 1. HTML ###
(https://github.com/farahramadhina/quidditch_supplies/assets/124555865/40853068-a81e-4d25-a608-6fcea8e1f205)

### 2. XML ###
(https://github.com/farahramadhina/quidditch_supplies/assets/124555865/62d6511b-ea47-451f-8592-6895ee4b7e99)

### 3. JSON ###
(https://github.com/farahramadhina/quidditch_supplies/assets/124555865/fd2bae29-86e0-43f3-ab1d-1d61b852d46e)

### 4. XML *by ID* ###
(https://github.com/farahramadhina/quidditch_supplies/assets/124555865/944fc824-f3b4-43bb-be0e-6cda9de33b49)

### 5. JSON *by ID* ###
(https://github.com/farahramadhina/quidditch_supplies/assets/124555865/3ffdda7a-3222-4a55-a99c-4caea84981e2)


# Tugas 2: Implementasi Model-View-Template (MVT) pada Django #
## Farah Dhiya Ramadhina/PBP B/2206082934 ##

## A. Implementasi Checklist *step-by-step* ##
### Membuat sebuah proyek Django baru. ###
* Membuat direktori baru dengan nama `quidditch_supplies` pada folder PBP Farah di Desktop, yang saya gunakan untuk menyimpan semua file PBP saya pada semester ini.
* Membuat *virtual environment* pada terminal direktori yang baru saya buat dengan menjalankan prompt berikut : `python -m venv env`
* Mengaktifkan virtual environment dengan prompt berikut : `source env/bin/activate` . Virtual environment akan aktif dan dapat terlihat dengan adanya `(env)` di awal baris input terminal
* Membuat berkas `requirements.txt` pada direktori yang baru kita buat, dan mengisi berkas tersebut dengan beberapa dependencies. Dependencies merupakan komponen atau modul yang diperlukan oleh suatu perangkat lunak untuk berfungsi, termasuk library, framework, atau package. 
* Menjalankan virtual environment, lalu memasang dependencies dengan menginput prompt berikut pada terminal : `pip install -r requirements.txt`
* Membuat proyek Django bernama `quidditch_supplies` dengan prompt : `django-admin startproject quidditch_supplies .`
* Buka `settings.py` yg ada di direktori yang telah saya buat, lalu menambahkan `"*"` pada `ALLOWED_HOSTS` menjadi
`ALLOWED_HOSTS = ["*"]`. Dengan menetapkan nilai `["*"]`, akan memungkinkan aplikasi saya diakses secara luas. 
* Memastikan bahwa berkas `manage.py` ada pada direktori yang aktif pada shell saya saat ini, lalu jalankan server Django dengan prompt berikut : `./manage.py runserver`
* Buka `http://localhost:8000/` pada browser untuk memastikan bahwa aplikasi Django saya berhasil dibuat (ditandai dengan adanya animasi roket dan teks yang bertuliskan installation succesful pada halaman yang dibuka)
* Aplikasi Django selesai dibuat. Tekan `Control+C` pada shell untuk menghentikan server, dan menonaktifkan virtual environment dengan prompt : `deactivate`

### Membuat aplikasi dengan nama 'main' pada proyek tersebut. ###
* Buka terminal pada direktori utama `quidditch_supplies`, lalu aktifkan virtual environment yang telah dibuat sebelumnya dengan menjalankan prompt berikut : `source env/bin/activate`
* Jalankan prompt berikut untuk membuat aplikasi baru bernama main : `python manage.py startapp main` 
* Buka berkas `settings.py` pada direktori proyek `quidditch_supplies`, lalu tambahkan `main` pada daftar aplikasi yg ada pada variabel `INSTALLED_APPS` untuk mendaftarkan aplikasi `main` ke dalam proyek.

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main. ###
* Buka berkas `urls.py` di dalam direktori proyek `quidditch_supplies` , bukan yang ada di dalam direktori aplikasi `main`
* Impor funhsi `include` dari `django.urls` .
* Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main dalam variabel `urlpatterns`
```ruby
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
* Jalankan proyek Django dengan prompt `python manage.py runserver`
* Buka `http://localhost:8000/main/` di browser untuk melihat page yang sudah dibuat

### Membuat model pada aplikasi 'main' dengan nama 'Item' dan memiliki atribut wajib sebagai berikut : 
`name` sebagai nama item dengan tipe `CharField`.
`amount' sebagai jumlah item dengan tipe `IntegerField`.
`description' sebagai deskripsi item dengan tipe `TextField`.
* Buka berkas `models.py` pada direktori aplikasi `main`
* Isi berkas `models.py` dengan menambahkan atribut wajib dan pilihan sesuai yang kita inginkan seperti berikut : 
```ruby
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
```

### Membuat sebuah fungsi pada 'views.py' untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. ###
* Buka berkas `views.py` pada berkas aplikasi `main`, lalu impor modul yg dibutuhkan untuk membuat fungsi `show_main` seperti berikut : 
`from django.shortcuts import render`
* Tambahkan fungsi 'show_main' di bawah baris impor yang akan dikembalikan dalam template HTML yang menampilkan nama dan kelas saya seperti berikut : 
```ruby
def show_main(request):
    context = {
        'name': 'Farah Dhiya Ramadhina',
        'class': 'PBP B'
    }
    return render(request, "main.html", context)
```

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. ###
* Buka berkas `urls.py` di dalam direktori `main`
* Isi `urls.py` dengan kode ini : 
```ruby
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. ###
* Buka Adaptable.io pada browser, login menggunakan GitHub, lalu tekan tombol `New App`.
* Pilih `Connect an Existing Repository`, dan pilih repositori proyek `quidditch_supplies` yang telah saya buat sebagai basis aplikasi yang akan di-deploy. Pilih branch `main` sebagai *deployment branch*.
* Pilih `Python App Template` sebagai *template deployment* dan `PostgreSQL` sebagai tipe basis data yang akan digunakan.
* Sesuaikan versi Python dengan spesifikasi python saya yaitu `3.11` dan pada bagian `Start Command` masukkan prompt `python manage.py migrate && gunicorn quidditch_supplies.wsgi.`
* Masukkan nama aplikasi yang akan menjadi nama domain situs web aplikasi, lalu centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi.


## B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. ##
(https://github.com/farahramadhina/quidditch_supplies/assets/124555865/c71d00be-0736-45ad-99f0-ee82abb27f7e)


## C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? ##
Virtual environment digunakan dalam membuat aplikasi web berbasis Django untuk menjaga kerapihan dan mengisolasi pengembangan perangkat lunak. Virtual environment memungkinkan kita untuk membuat lingkungan terisolasi di mana kita dapat menginstal dan mengelola dependencies secara independen untuk setiap proyek. Hal ini dapat mencegah konflik *compatibility issues* jika kita memiliki beberapa proyek yang berbagi dependencies yang sama dengan versi yang berbeda. Dengan virtual environment, kita dapat menggunakan pip (Python Package Manager) untuk dengan mudah menginstal, menghapus, dan mengelola paket Python yang diperlukan untuk proyek tertentu tanpa mempengaruhi paket-paket di luar lingkungan tersebut. 

Kita sebenarnya bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi hal ini berisiko. Tanpa virtual environment, paket Python akan diinstal secara global di komputer kita, yang bisa menyebabkan masalah jika kita bekerja pada beberapa proyek yang menggunakan versi paket yang berbeda. Oleh karena itu, lebih baik menggunakan virtual environment dalam pengembangan Django dan Python agar proyek kita lebih rapi dan terhindar dari masalah.

## D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. ##
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah cara berbeda untuk merancang dan memisahkan komponen dalam pengembangan perangkat lunak:

1. **MVC (Model-View-Controller)**:
   - **Model**: Menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
   - **View**: Menampilkan informasi kepada pengguna dalam bentuk *Graphical User Interface* (GUI).
   - **Controller**: Menghubungkan serta mengatur model dan view agar dapat saling terhubung.

2. **MVT (Model-View-Template)**:
   - **Model**: Menghubungkan aplikasi dengan basis data dan mengatur interaksi dengan data tersebut.
   - **View**: Mengatur tampilan dan mengambil data dari model untuk ditampilkan ke pengguna.
   - **Template**: Merancang tampilan yang akan diisi dengan data dari model melalui view.

3. **MVVM (Model-View-ViewModel)**:
   - **Model**: Mengelola data.
   - **View**: Menampilkan informasi.
   - **ViewModel**: Menengahi antara Model dan View, menyiapkan data dan mengelola tindakan pengguna.

Perbedaan ketiganya adalah MVC menggunakan Controller sebagai perantara, MVT menggunakan Template untuk tampilan, dan MVVM memperkenalkan ViewModel untuk mengelola data dan tampilan. Pilihan tergantung pada preferensi dan kebutuhan dalam mengembangkan aplikasi.