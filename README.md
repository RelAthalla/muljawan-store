# muljawan-store

# Tugas 2

1. Membuat project django baru

Pertama-tama, saya akan membuat repositori baru di github saya. Lalu saya membuat direktori lokal untuk memulai project saya. Lalu saya akan menghubungkan direktori lokal saya dengan repositori github dengan beberapa command yaitu git init untuk menginisiasi penggunaan git, git branch -M main untuk membuat branch main, git remote add origin <URL_REPO> untuk menghubungkan repositori lokal dan github. Setelah itu saya mengaktifkan virtual environment pada direktori saya dengan command python -m venv env lalu command env\Scripts\activate. Guna virtual environtment adalah untuk mengisolasi package serta dependency agar tidak bertabrakan dengan versi lain pada komputer saya. Selanjutnya saya menyiapkan beberapa dependencies pada projek saya yaitu ada django, gunicorn, whitenoise, psycopg2-binary
, requests, urllib3 dalam sebuah textfile yang saya beri nama requirements.txt. Lalu saya menginstall dependencies yang telah saya masukan ke textfile dengan command pip install -r requirements.txt. Selanjutnya saya membuat struktur awal dari project saya secara automatis menggunakan command django-admin startproject muljawan_store. Lalu saya membuka settings.py untuk menambahkan host local di allowed host untuk melihat apakah ada masalah dalam pembuatan project saya. Untuk menjalankan di local host pastikan di allowed host sudah di setting dan tinggal jalankan command python manage.py runserver. Lalu saya tambahkan berkas .gitignore guna menentukan berkas yang harus diabaikan oleh git contohnya seperti environtment. Selanjutnya saya melakukan add, commit, dan push ke repositori github saya

2. Membuat aplikasi bernama main dalam project

Saya membuat aplikasi main dengan perintah python manage.py startapp main yang akan membuat struktur awal dari aplikasi saya. Setelah itu saya menambahkan main ke dalam daftar aplikasi di project saya dengan cara masuk ke settings.py lalu pada variabel INSTALLED_APPS tambahkan ‘main’

3. Melakukan routing pd proyek

Selanjutnya konfigurasi routing pada URL pada projek saya. Langkah awal yang dilakukan adalah mengimpor path dan include dari dhango.urls lalu membuat variable urlspatterns yang merupakan sebuah list untuk menampung rute url. Lalu saya mengimpor url dari aplikasi yang telah kita buat dengan fungsi path dan didalamnya terdapat fungsi include yang gunanya untuk mengimpor rute url dari aplikasi lain. Disini kita baru hanya mengimpor satu aplikasi yaitu main 

4. Membuat model pada aplikasi main 

Saya membuat model pada aplikasi main dengan nama Product dan memiliki atribut name, price, dan description dengan cara membuat class Product dengan parameter models.Model untuk mendifinisikan model. Lalu name saya definisikan sbg CharField, price sebagai IntegerField, dan description sebagai TextField. Setiap membuat perubahan pd model, saya akan membuat migrasi model dengan cara menjalancan command python manage.py makemigrations dan python manage.py migrate. Kedua command ini berguna untuk menerapkan migrasi ke basis data lokal(berkas migrasi) dan mengaplikasikan perubahan yang terdapat dalam berkas migrasi.

5. Menambahkan fungsi pada views.py

Di dalam views.py, saya menambahkan impor untuk render dan sebuah fungsi yaitu show_main dengan parameter request. Fungsi tersebut beguna untuk untuk mengatur request dari HTTP dan menampilakn tampilan yang sesuai. Fungsi akan me return fungsi render yang beguna untuk me render tampilan main.html. Fungsi render memiliki 3 parameter yang masing masing menerima request dari http, berkas html untuk merender tampilan, dan data yang diteruskan ke tampilan berupa dictionary

6. Routing pd aplikasi main

Saya melakukan routing URL aplikasi main saya dengan cara membuka urls.py dalam aplikasi main, lalu menambahkan beberapa code yang berguna untuk mengimpor path dari django.urls, mengimpor method show_main dari views.py, lalu membuat variable untuk menyimpan ‘main’, dan membuat list urlspattern yang didalamnya menggunakan fungsi path untuk mendefinisikan pola URL yang menggunakan fungsi show_main untuk memunculkan tampilan ketika URL terkait diakses.

7. Melakukan deployment ke PWS

Pertama saya membuat akun PWS saya lalu membuat project baru. Setelah itu akan muncul project credentials yang harus saya simpan. Lalu pada allowed_host yang terdapat di settings.py tambahkan URL dari deployment PWS. Lalu untuk launching, jalankan perintah yang terdapat di project command yaitu untuk push ke branch master dimana master itu sendiri adalah PWS-nya. Project yang sudah berjalan akan terdapat status running warna hijau. Jika kedepannya terdapat perubahan, saya hanya tinggal push dari main ke master dengan command git push pws main:master.

8. Kaitan Antar Komponen

urls.py bertugas memetakan URL yang diminta oleh client ke fungsi yang sesuai di views.py.
views.py memproses request, mengambil data dari models.py, dan meneruskan data tersebut ke template HTML.
models.py berhubungan dengan database dan digunakan oleh views.py untuk mengambil atau menyimpan data.
Template HTML digunakan untuk menampilkan data yang diambil dari database dalam format yang bisa dilihat oleh pengguna.
![](<bagan/MVT Django.jpeg>)

9. Fungsi GIT dalam pengembangan perangkat lunak

Ada beberapa fungsi git dalam pengembangan perangkat lunak, beberapa fungsinya adalah:
    1. Manajemen Versi (Version Control): Git memungkinkan pengembang melacak perubahan dalam kode secara terperinci. Setiap kali perubahan dilakukan, Git menyimpan "snapshot" kode tersebut, sehingga memungkinkan untuk kembali ke versi sebelumnya jika diperlukan.
    2. Kolaborasi Tim: Git memfasilitasi kerja kolaboratif dalam tim pengembang. Setiap anggota tim dapat bekerja pada fitur atau perbaikan bug secara independen dalam "branch" terpisah, kemudian menggabungkan perubahan mereka ke branch utama setelah selesai dan diuji.
    3. Branching dan Merging: Git memungkinkan pembuatan branch (cabang) untuk pengembangan fitur baru atau perbaikan bug. Ini membantu memisahkan pekerjaan pengembangan dari kode yang sudah stabil. Setelah fitur selesai, Git mempermudah proses merge untuk menggabungkan perubahan ke kode utama.
    4. Backup dan Pemulihan: Setiap kali kode disimpan di Git, perubahan tersebut dapat di-push ke repositori yang disimpan secara remote (misalnya GitHub, GitLab, atau Bitbucket), sehingga berfungsi sebagai cadangan (backup). Selain itu, pengembang bisa memulihkan versi sebelumnya jika terjadi kesalahan.
    5. Audit dan Sejarah: Git menyimpan log semua perubahan yang dilakukan, termasuk siapa yang melakukan perubahan dan kapan. Ini membantu untuk melacak kesalahan atau memahami keputusan yang diambil pada masa lalu.
    6. Integrasi dengan CI/CD: Git sering diintegrasikan dengan pipeline Continuous Integration/Continuous Deployment (CI/CD), yang membantu dalam otomatisasi build, pengujian, dan deployment kode setelah setiap perubahan.

10. mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dipilih sebagai media pembelajaran perangkat lunak terutama aplikasi web bukan tanpa alasan. Di Django semua fitur sudah siap pakai, seperti contoh saya diatas saat ingin membuat sebuah project, saya tinggal menjalankan command django-admin startproject muljawan_store. Ini memudahkan pemula seperti saya karena tidak perlu mengkonfigurasi atau memasang terlalu banyak komponen eksternal untuk memulai proyek. Django memiliki arsitektur yang terstruktur dengan jelas berdasarkan pola Model-View-Template (MVT), ini memudahkan saya dalam memahami bagaimana berbagai bagian aplikasi berinteraksi. Ini memudahkan untuk membangun dan memelihara aplikasi yang lebih besar seiring waktu. Django juga memiliki dokumentasi yang mendetail, ini memudahkan saya untuk memahami konsep dan fitur framework. Saya juga tertarik karena komunitasnya yang sudah besar jadi mudah mencari solusi jika terdapat suatu problem dan juga banyak plugin dan ekstensi yang memudahkan pengembang untuk menanmbahkan fitur baru. Django juga dikenal dengan "conventuon over configuration" ini artinya pemula dapat fokus pada pengembangan fitur aplikasi tanpa terbebani oleh konfigurasi yang rumit. Django digunakan oleh beberapa platform populer seperti Instagram, Pinterest, dan Mozilla, yang menunjukkan bahwa belajar Django memiliki relevansi nyata di industri. Ini memberikan motivasi tambahan bagi pemula, karena apa yang mereka pelajari dapat diterapkan dalam pengembangan aplikasi web yang nyata.

11. Mengapa model pada Django disebut sebagai ORM?

ORM (Object-Relational Mapping) adalah sebuah teknik yang memungkinkan pengembang untuk berinteraksi dengan basis data relasional menggunakan paradigma pemrograman berorientasi objek. Dalam konteks Django, model disebut sebagai ORM karena mereka berfungsi sebagai perantara antara kode Python dan basis data relasional. Berikut adalah penjelasan lebih rinci mengenai mengapa model pada Django disebut sebagai ORM:
    1. Pemetaaan Objek ke Tabel Relasional
    Django models adalah representasi dari tabel dalam basis data. Setiap kelas model di Django mewakili satu tabel, dan setiap atribut dalam kelas tersebut mewakili kolom dalam tabel tersebut.
    2. Abstraksi Basis Data
    Dengan menggunakan ORM, pengembang dapat melakukan operasi basis data (seperti CRUD—Create, Read, Update, Delete) menggunakan objek dan metode Python tanpa perlu menulis SQL secara langsung.
    3. Manajemen Relasi antar Tabel
    Django ORM memudahkan pengelolaan relasi antar tabel seperti one-to-one, one-to-many, dan many-to-many tanpa harus menulis join SQL secara manual.
    4. Keamanan dan Validasi
    Django ORM secara otomatis menangani sanitasi input dan parameterisasi query, yang membantu mencegah serangan SQL injection. Selain itu, model Django menyediakan mekanisme validasi data yang memastikan integritas data sebelum disimpan ke basis data.
    5. Portabilitas dan Migrasi
    Dengan menggunakan ORM, aplikasi Django menjadi lebih portabel antar berbagai sistem basis data (seperti PostgreSQL, MySQL, SQLite, dll.) tanpa perlu mengubah kode query. Selain itu, Django menyediakan sistem migrasi yang memudahkan pengelolaan perubahan skema basis data berdasarkan perubahan model.
    6. Query Abstraksi dan Optimasi
    Django ORM menyediakan API tingkat tinggi untuk menulis query kompleks dengan cara yang lebih mudah dan terstruktur.
    7. Produktivitas dan Pemeliharaan Kode
    Dengan ORM, pengembang dapat menulis kode yang lebih bersih, terstruktur, dan mudah dipelihara. Hal ini meningkatkan produktivitas karena mengurangi kebutuhan untuk menulis dan memelihara SQL mentah, serta meminimalkan kemungkinan kesalahan dalam query.
Model pada Django disebut sebagai ORM karena mereka menyediakan lapisan abstraksi yang menghubungkan objek Python dengan tabel dan relasi dalam basis data relasional. Dengan demikian, Django ORM memungkinkan pengembang untuk bekerja dengan basis data secara lebih efisien, aman, dan terstruktur menggunakan paradigma berorientasi objek, tanpa harus terlibat langsung dengan kompleksitas SQL.

# Tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dalam pengimplementasian sebuah platform sangat penting karena hal ini memastikan bahwa data yang dihasilkan atau diambil oleh platform dapat diakses dan digunakan secara efektif oleh pengguna akhir. Ada beberapa alasan mengapa data delivery diperlukan:

    1. Ketersediaan dan Aksesibilitas

    2. Keandalan

    3. Kinerja dan Efisiensi

    4. Pengalaman Pengguna

    5. Sinkronisasi dan Kolaborasi

    6. Keamanan

    7. Kompatibilitas Antar Sistem

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Saya memilih JSON karena cenderung lebih populer dibandingkan XML. Berikut ini adalah perbandingan antara keduanya dan alasan mengapa JSON lebih banyak digunakan.

    1. Struktur dan Sintaks
    JSON lebih sederhana dan mudah dibaca oleh manusia, serta ukuran datanya lebih kecil dibandingkan XML, yang memerlukan tag pembuka dan penutup pada setiap elemen.

    2. Ukuran Data
    JSON meminimalkan overhead dalam pertukaran data, membuatnya lebih cepat untuk dikirim dan diambil, terutama pada aplikasi web atau API yang mengutamakan efisiensi.

    3. Kompatibilitas dengan JavaScript
    JSON dapat langsung digunakan dalam JavaScript tanpa konversi tambahan, JSON sangat efisien untuk aplikasi web modern yang sering menggunakan JavaScript di sisi client.

    4. Kemudahan Parsing dan Penanganan Data
    JSON lebih cepat untuk diproses, sehingga lebih efisien terutama dalam aplikasi web yang memerlukan respons cepat.

    5. Penggunaan dan Ekosistem Modern
    Dengan banyaknya API yang menggunakan JSON, serta tren pengembangan web yang lebih mengutamakan kesederhanaan dan kecepatan, JSON lebih relevan untuk penggunaan saat ini.

    6. Kemampuan untuk Merepresentasikan Tipe Data
    JSON lebih efisien dalam menangani tipe data yang berbeda, yang membuatnya lebih fleksibel dan mudah digunakan.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method ini memeriksa data yang dimasukkan ke dalam form, membandingkannya dengan aturan validasi yang telah ditentukan pada setiap field. Misalnya, untuk field yang harus berisi email, is_valid() akan memastikan bahwa input tersebut adalah alamat email yang valid. Selain memeriksa format, method ini juga mengecek apakah semua field yang wajib diisi (required=True) sudah diisi oleh pengguna. Jika ada field yang kosong tapi seharusnya diisi, form dianggap tidak valid. Jika form tidak valid, method ini akan mengisi atribut errors pada form dengan pesan error yang sesuai. Pesan ini bisa digunakan untuk memberi tahu pengguna apa yang salah dengan input mereka.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token digunakan untuk melindungi aplikasi Django dari serangan CSRF. Ini dilakukan dengan menambahkan token yang unik dan hanya berlaku untuk sesi pengguna tertentu ke dalam setiap form yang dikirimkan ke server. Saat form tersebut dikirim, token ini diverifikasi oleh server untuk memastikan bahwa permintaan tersebut sah dan berasal dari pengguna yang valid. Token ini secara otomatis dibuat oleh Django dan disisipkan ke dalam form sebagai input tersembunyi atau ke dalam header HTTP (jika menggunakan AJAX). Server akan memeriksa apakah token yang diterima cocok dengan token yang disimpan di sisi server untuk memastikan permintaan tidak dimanipulasi oleh pihak ketiga. Django memiliki mekanisme otomatis untuk memproteksi seluruh view yang memproses permintaan POST. Jika form POST dikirim tanpa csrf_token yang valid, server akan menolak permintaan tersebut sebagai tindakan pencegahan. 

Jika csrf_token tidak disertakan dalam form, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat mengambil keuntungan dari kondisi ini untuk membuat pengguna yang terautentikasi melakukan aksi yang tidak diinginkan.

Contoh Skenario Serangan Tanpa csrf_token:
Seorang pengguna sudah login ke akun perbankannya. Penyerang mengirimkan email berisi link ke halaman jahat yang berisi form tersembunyi yang memerintahkan transfer dana ke akun milik penyerang.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. membuat base.html dalam templates untuk menjadi page utama
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% block meta %} {% endblock meta %}
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>
    ```

    2. Menambahkan `BASE_DIR` pada `settings.py` agar project mengenali html yang akan menjadi template utama
    ```python
    'DIRS': [BASE_DIR / 'templates'],
    ```

    3. Menambahkan atribut `time` dan `id` pada model product
    ```python
    from django.db import models
    import uuid

    class ProductEntry(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField()
        time = models.DateField(auto_now_add=True)
    ```

    4. Membuat `forms.py` untuk mendeklarasikan atribut-atribut dari model yang membutuhkan input dari user
    ```python
    from django.forms import ModelForm
    from .models import ProductEntry

    class ProductEntryForm(ModelForm):
        class Meta:
            model = ProductEntry
            fields = ["name", "price", "description", "quantity"]
    ```

    5. Membuat method `create_product_entry` untuk mengambil input user sesuai dengan `forms.py`
    ```python
    def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
    ```

    6. Membuat method `show_main` untuk menampilkannya di `main.html`
    ```python
    def show_main(request):
    product_entries = ProductEntry.objects.all()
    
    context = {
        'name' : 'Farrel Athalla Muljawan',
        'class': 'E',
        'product': product_entries
    }

    return render(request, "main.html", context)
    ```

    7. Membuat `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk menampilkan response back dari input user
    ```python
    def show_xml(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

    def show_json(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("json",data),content_type='application/json')

    def show_xml_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    8. Melakukan routing di dari method yang sudah dibuat di `urls.py`
    ```python
    from django.urls import path, include
    from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product-entry', create_product_entry, name='create_product_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

    10. Membuat `create_name_entry.html` untuk tampilan ketika web ingin meminta input dari pengguna
    ```python
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
    
    11. Membuat `main.html` untuk menampilkan product dari hasil input pengguna
    ```python
        {% extends 'base.html' %}
        {% block content %}
        <h1>Muljawan Store</h1>
        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>Class: </h5>
        <p>{{ class }}<p>

        ...
        {% if not product %}
        <p>Belum ada data produk pada muljawan store.</p>
        {% else %}
        <table>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Description</th>
                <th>Quantity</th>
                <th>Time</th>
            </tr>

            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini 
            {% endcomment %} 
            {% for product_entry in product %}
            <tr>
                <td>{{product_entry.name}}</td>
                <td>{{product_entry.price}}</td>
                <td>{{product_entry.description}}</td>
                <td>{{product_entry.quantity}}</td>
                <td>{{product_entry.time}}</td>
            </tr>
            {% endfor %}
        </table>
        {% endif %}

        <br />

        <a href="{% url 'main:create_product_entry' %}">
            <button>Add New Product Entry</button>
        </a>

        {% endblock content %}
    ```

6. Screenshot postman
![](bagan/XML.png)
![](bagan/JSON.png)
![](<bagan/XML ID.png>)
![](<bagan/JSON ID.png>)