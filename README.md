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

# Tugas 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

perbedaan keduanya adalah HttpResponseRedirect() digunakan ketika kamu ingin langsung mengembalikan pengalihan ke URL tertentu. Sedangkan redirect() adalah versi yang lebih ringkas dan fleksibel, yang memungkinkan pengalihan menggunakan URL, view name, atau object. 

2. Jelaskan cara kerja penghubungan model Product dengan User!

Penghubungan model Product dengan User dalam Django umumnya dilakukan untuk menunjukkan bahwa setiap produk (Product) memiliki relasi dengan pengguna (User). Ini biasanya digunakan dalam skenario di mana pengguna dapat membuat, mengelola, atau memiliki produk. Berikut adalah cara kerja dan langkah-langkah dalam menghubungkan kedua model ini.

    1. Membuat Model Product dan User
Django sudah menyediakan model User bawaan melalui modul django.contrib.auth.models. Jadi, untuk menghubungkan model Product ke User, kita cukup membuat model Product dan menambahkan relasi ke model User.

    2. ForeignKey (Relasi Many-to-One)
Untuk setiap produk yang dimiliki atau dikelola oleh satu pengguna, kita bisa menggunakan ForeignKey di model Product. Ini berarti satu pengguna bisa memiliki banyak produk, tetapi satu produk hanya dapat dimiliki oleh satu pengguna.

contoh model product:
    ```python
    class ProductEntry(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField()
        time = models.DateField(auto_now_add=True)
    ```
3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

    1. Authentication (Autentikasi)
    Pengertian: Autentikasi adalah proses memverifikasi identitas seorang pengguna. Dengan kata lain, ini adalah proses untuk memastikan bahwa pengguna benar-benar siapa yang dia klaim. Biasanya, ini dilakukan dengan meminta kombinasi username/email dan password saat pengguna login.
    Contoh sederhana: Ketika pengguna memasukkan username dan password, sistem akan mengecek apakah informasi tersebut cocok dengan data pengguna yang ada di sistem.

    Django menyediakan modul django.contrib.auth yang menangani autentikasi pengguna.
    Saat pengguna login, Django menggunakan fungsi authenticate() dan login() untuk mengautentikasi pengguna:
    authenticate(request, username, password): Fungsi ini memeriksa apakah username dan password yang diberikan valid. Jika valid, fungsi akan mengembalikan objek User. Jika tidak, akan mengembalikan None.
    login(request, user): Setelah berhasil diautentikasi, login() digunakan untuk memasukkan informasi pengguna ke sesi, sehingga pengguna dianggap login.

    2. Authorization (Otorisasi)
    Pengertian: Otorisasi adalah proses menentukan izin atau hak yang dimiliki pengguna setelah berhasil diautentikasi. Setelah sistem mengetahui siapa pengguna tersebut (melalui autentikasi), otorisasi digunakan untuk menentukan apa yang diizinkan untuk dilakukan pengguna tersebut, seperti mengakses halaman tertentu, mengedit data, atau menghapus konten.
    Contoh sederhana: Misalnya, seorang pengguna yang berhasil login mungkin tidak memiliki akses untuk menghapus artikel, tetapi hanya bisa melihat dan mengedit artikel.

    Django juga menangani otorisasi melalui modul django.contrib.auth, yang memungkinkan untuk menentukan permissions dan groups.
    Django memiliki sistem permissions bawaan yang terintegrasi dengan model. Setiap model di Django secara otomatis mendapatkan tiga permissions:
    add_<model>,
    change_<model>,
    delete_<model>.
    Permissions bisa diperiksa menggunakan method seperti has_perm() atau decorator seperti @permission_required.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

    Ketika pengguna login, Django menggunakan mekanisme session dan cookies untuk mengingat pengguna di antara permintaan HTTP yang berbeda (HTTP adalah protokol stateless, artinya setiap permintaan HTTP tidak "mengingat" permintaan sebelumnya). Berikut adalah bagaimana proses ini bekerja:

    Setelah pengguna berhasil diautentikasi (login), Django menyimpan informasi sesi di database atau tempat penyimpanan lainnya (seperti memcached atau cache file).
    Django mengirimkan session ID ke browser pengguna sebagai cookie yang disimpan di browser. Cookie ini berisi ID unik yang menghubungkan browser pengguna dengan sesi yang tersimpan di server.
    Pada setiap permintaan berikutnya, browser pengguna mengirimkan cookie yang berisi session ID tersebut kembali ke server Django.
    Django kemudian menggunakan session ID ini untuk mengambil data sesi pengguna yang tersimpan di server, termasuk informasi bahwa pengguna telah login.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Membuat form register menggunakan UserCreationForm dari django.contrib.auth.forms di views.py aplikasi main
    ```python
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```

    2. Membuat register.html dalam template di direktori main
    ```python
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}

    <div class="login">
        <h1>Register</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar" /></td>
                </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
    </div>

    {% endblock content %}
    ```

    3. Menambahkan function urls.py
    ```python
    path('register/', register, name='register'),
    ```

    4. Membuat form login menggunakan AuthenticationForms dari django.contrib.auth.forms dan method authenticate dan login dari django.contrib.auth di views.py aplikasi main.
    ```python
    def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
    ```

    5. Membuat login.html sebagai template dari form login di dalam aplikasi main.
    ```python
    {% extends 'base.html' %}
    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    ```

    6. Menambahkan urls.py untuk login
    ```python
    path('login/', login_user, name='login'), 
    ```

    7. Membuat method logout_user
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        print("Logout successful, redirecting to login page") 
        return response
    ```

    8. Menambahkan pada urls.py
    ```python
    path('logout/', logout_user, name='logout_user'),
    ```

    9. Menambahkan button logout pada main.html
    ```python
    <a href="{% url 'main:logout_user' %}">
        <button>Logout</button>
    </a>
    ```

    10. Mengubah isi dari baris pada show_main
    ```python
    products = Product.objects.filter(user=req.user)
    ```


6. Screenshot dari user dengan 3 dummy data
![](bagan/User1.png)
![](bagan/User2.png)

# Tugas 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

    Dalam CSS, ketika beberapa selector diterapkan pada elemen HTML yang sama, prioritas (atau specificity) akan menentukan aturan mana yang diambil. Berikut adalah urutan prioritas CSS selector:

    1. Inline Style (paling tinggi)

    Jika CSS ditulis langsung dalam atribut elemen HTML menggunakan style="", maka gaya ini akan selalu diutamakan.
    Contoh: <div style="color: red;"></div>.

    2. ID Selector (#id)

    Selector yang menggunakan ID memiliki prioritas lebih tinggi daripada class, attribute, atau type selector.
    Contoh: #myID { color: blue; }.

    3. Class, Attribute, dan Pseudo-Class Selector (.class, [attribute], :hover, dll.)

    Class selector atau selector berbasis atribut, serta pseudo-class seperti :hover, memiliki prioritas di bawah ID, tetapi di atas type selector.
    Contoh: .myClass { color: green; } atau [type="text"] { color: green; }.

    4. Type Selector (tag HTML seperti div, p, dll.) dan Pseudo-Element Selector (::before, ::after)

    Ini memiliki prioritas paling rendah di antara selector lainnya.
    Contoh: div { color: black; } atau ::before { content: ""; }.

    5. Universal Selector (*)

    Selector ini memiliki prioritas paling rendah dan diterapkan pada semua elemen.
    Contoh: * { margin: 0; }.

    6. !important (mengabaikan urutan prioritas di atas)

    Jika suatu aturan memiliki deklarasi !important, itu akan mengesampingkan aturan lain yang tidak menggunakan !important, terlepas dari tingkat spesifisitas.
    Contoh: p { color: red !important; }.
    Contoh Perhitungan Prioritas

    Jika ada beberapa selector yang berlaku untuk elemen yang sama, urutan prioritas dihitung sebagai berikut:

    Inline styles (1000)
    ID selector (100)
    Class, pseudo-class, dan attribute selector (10)
    Type selector dan pseudo-element (1)

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

    Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memungkinkan situs web untuk tampil dan berfungsi dengan baik di berbagai perangkat, mulai dari desktop dengan layar besar hingga smartphone dengan layar kecil. Ada beberapa alasan mengapa responsive design menjadi krusial:

    1. Peningkatan Penggunaan Perangkat Mobile
    Pengguna internet semakin banyak mengakses web melalui smartphone dan tablet. Dengan desain responsif, situs web dapat menyesuaikan tampilannya agar mudah dibaca dan dinavigasi di layar kecil, sehingga pengalaman pengguna (UX) menjadi lebih baik.

    2. Pengalaman Pengguna yang Konsisten
    Responsive design memastikan bahwa pengguna mendapatkan tampilan dan pengalaman yang konsisten di berbagai perangkat, tanpa perlu membuat versi terpisah untuk mobile dan desktop.

    3. SEO yang Lebih Baik
    Google dan mesin pencari lainnya lebih memprioritaskan situs yang ramah terhadap perangkat mobile (mobile-friendly). Situs yang tidak responsif mungkin tidak mendapatkan peringkat yang baik di hasil pencarian.

    4. Efisiensi Biaya dan Waktu
    Daripada membuat beberapa versi dari satu situs web untuk berbagai perangkat (seperti versi mobile, tablet, atau desktop), responsive design memungkinkan satu desain fleksibel yang bekerja di semua perangkat. Ini menghemat biaya pengembangan dan pemeliharaan.

    5. Adaptasi ke Berbagai Ukuran Layar
    Dengan munculnya berbagai perangkat dengan ukuran layar yang berbeda (laptop, tablet, phablet, smartwatch), responsive design membuat situs tetap tampil optimal pada berbagai resolusi tanpa memerlukan perubahan drastis.
    Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
    Twitter:

    Twitter menerapkan responsive design secara sempurna. Baik di desktop, tablet, atau smartphone, antarmuka pengguna menyesuaikan diri dengan ukuran layar, memastikan kemudahan penggunaan dan navigasi di setiap perangkat.
    Airbnb:

    Aplikasi dan situs web Airbnb memiliki desain responsif yang baik, memberikan pengalaman yang hampir sama, baik di desktop maupun perangkat mobile, dengan tampilan yang disesuaikan sesuai ukuran layar.
    Netflix:

    Netflix memungkinkan pengguna menikmati konten di perangkat apapun dengan antarmuka yang menyesuaikan sesuai ukuran layar. Situs dan aplikasi Netflix dirancang responsif untuk memberikan pengalaman menonton terbaik.
    Contoh Aplikasi yang Belum Menerapkan Responsive Design:
    Situs Web Lawas Pemerintah:

    Beberapa situs web pemerintah lama belum menerapkan desain responsif dan mungkin terlihat berantakan ketika diakses melalui perangkat mobile. Misalnya, situs yang didesain lebih dari satu dekade lalu biasanya tidak memperhitungkan tampilan mobile.
    Beberapa Situs Berita Kecil:

    Situs berita kecil atau lokal yang belum memperbarui desain mereka cenderung hanya dioptimalkan untuk desktop. Saat diakses di smartphone, pengguna mungkin perlu memperbesar atau menggulir secara horizontal untuk membaca konten dengan jelas.
    Kesimpulan:
    Responsive design memastikan aplikasi web atau situs web tetap relevan di era digital, di mana akses melalui perangkat mobile mendominasi. Aplikasi yang tidak menerapkan responsive design akan memberikan pengalaman pengguna yang buruk, yang dapat mengakibatkan penurunan traffic dan peringkat pencarian.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

    Margin, border, dan padding adalah tiga properti CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML. Berikut penjelasan masing-masing, serta cara mengimplementasikannya:

    1. Margin
    Definisi: Margin adalah ruang di luar batas elemen. Ini digunakan untuk memberi jarak antara elemen dan elemen lain di sekitarnya.
    Fungsi: Mengatur jarak antar elemen. Margin tidak memiliki warna dan tidak mempengaruhi ukuran elemen.

    2. Border
    Definisi: Border adalah garis yang mengelilingi elemen, terletak di antara padding dan margin. Border dapat memiliki berbagai gaya, ketebalan, dan warna.
    Fungsi: Mengidentifikasi atau memisahkan elemen. Border dapat membuat elemen lebih menonjol.

    3. Padding
    Definisi: Padding adalah ruang di dalam elemen, antara konten elemen dan batas elemen (border). Padding mempengaruhi ukuran total elemen.
    Fungsi: Menambah ruang di dalam elemen agar konten tidak terlalu dekat dengan batas.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

    Flexbox dan Grid Layout adalah dua model layout CSS yang dirancang untuk membuat tata letak responsif dan fleksibel pada halaman web. Masing-masing memiliki kegunaan dan keunggulan tertentu. Berikut penjelasan mengenai kedua konsep tersebut:

    1. Flexbox (Flexible Box Layout)
    Konsep: Flexbox adalah model layout satu dimensi yang dirancang untuk mengatur elemen dalam satu baris (horizontal) atau satu kolom (vertikal). Dengan menggunakan flexbox, elemen dapat dengan mudah disusun dan diratakan, serta ruang di antara elemen dapat dikelola secara efisien.

    Cara Kerja:

    Kontainer Flex: Elemen yang menggunakan flexbox diatur dalam sebuah kontainer yang memiliki properti display: flex.
    Item Flex: Elemen di dalam kontainer menjadi item flex yang dapat diatur menggunakan berbagai properti untuk kontrol posisi, ukuran, dan ruang.
    Properti Utama:

    display: flex: Mengubah elemen menjadi kontainer flex.
    flex-direction: Mengatur arah item flex (row, column, row-reverse, column-reverse).
    justify-content: Mengatur perataan item di sepanjang sumbu utama (start, end, center, space-between, space-around).
    align-items: Mengatur perataan item di sepanjang sumbu silang (flex-start, flex-end, center, baseline, stretch).
    Kegunaan:

    Flexbox sangat berguna untuk layout sederhana seperti navigasi, menu, atau form.
    Memudahkan pengaturan responsif di mana elemen dapat menyesuaikan diri dengan ukuran kontainer yang tersedia.

    2. Grid Layout
    Konsep: Grid Layout adalah model layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Dengan grid, Anda dapat membuat tata letak yang lebih kompleks dengan mengatur elemen dalam grid yang telah ditentukan.

    Cara Kerja:

    Kontainer Grid: Elemen yang menggunakan grid diatur dalam sebuah kontainer yang memiliki properti display: grid.
    Item Grid: Elemen di dalam kontainer menjadi item grid yang dapat diletakkan pada posisi tertentu dalam grid.
    Properti Utama:

    display: grid: Mengubah elemen menjadi kontainer grid.
    grid-template-columns: Menentukan jumlah dan ukuran kolom.
    grid-template-rows: Menentukan jumlah dan ukuran baris.
    grid-gap: Mengatur jarak antara baris dan kolom.
    grid-area: Menentukan area tertentu di dalam grid untuk item grid.
    Kegunaan:

    Grid layout sangat berguna untuk desain tata letak yang kompleks, seperti tata letak halaman, card layout, atau grid image.
    Memudahkan pembuatan layout responsif yang dapat menyesuaikan elemen secara dinamis dengan ukuran layar yang berbeda.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Menambahkan dua function di views.py, yaitu delete_product dan edit_product yang bisa diterapkan pada setiap productnya.
    ```python
    def delete_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    mood.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

    def edit_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_product.html", context)
    ```

    2. Melakukan routing dari kedua function ini ke urls.py
    ```python
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    ```
    3. Pada base.html menambahkan beberapa code untuk responsive design web dan juga tailwind css
    ```python
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.tailwindcss.com"></script>
    ```

    4. Membuat global.css
    ```python
        .form-style form input, form textarea, form select {
        width: 100%;
        padding: 0.5rem;
        border: 2px solid #bcbcbc;
        border-radius: 0.375rem;
    }
    .form-style form input:focus, form textarea:focus, form select:focus {
        outline: none;
        border-color: #674ea7;
        box-shadow: 0 0 0 3px #674ea7;
    }
    @keyframes shine {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    .animate-shine {
        background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
        background-size: 200% 100%;
        animation: shine 3s infinite;
    }
    ```

    5. membuat navbar baru (punya saya belum fungsional)
    ```python
    <nav class="bg-gradient-to-b from-gray-800 via-gray-900 to-black shadow-lg fixed top-0 left-0 z-40 w-screen">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-3xl font-bold text-center text-gold font-medieval">Muljawan Store</h1>
                </div>
                <div class="hidden md:flex items-center space-x-4">
                    <a href="#" class="text-gray-300 hover:text-white transition duration-300">Home</a>
                    <a href="#" class="text-gray-300 hover:text-white transition duration-300">Products</a>
                    <a href="#" class="text-gray-300 hover:text-white transition duration-300">Categories</a>
                    <a href="#" class="text-gray-300 hover:text-white transition duration-300">Cart</a>
                    {% if user.is_authenticated %}
                        <span class="text-gray-300">Welcome, {{ user.username }}</span>
                        <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                            Logout
                        </a>
                    {% else %}
                        <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300 mr-2">
                            Login
                        </a>
                        <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                            Register
                        </a>
                    {% endif %}
                </div>
                <div class="md:hidden flex items-center">
                    <button class="mobile-menu-button">
                        <svg class="w-6 h-6 text-gold" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                            <path d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile menu -->
        <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
            <div class="pt-2 pb-3 space-y-1 mx-auto">
                <a href="#" class="block text-gray-300 px-3 py-2 hover:text-white transition duration-300">Home</a>
                <a href="#" class="block text-gray-300 px-3 py-2 hover:text-white transition duration-300">Products</a>
                <a href="#" class="block text-gray-300 px-3 py-2 hover:text-white transition duration-300">Categories</a>
                <a href="#" class="block text-gray-300 px-3 py-2 hover:text-white transition duration-300">Cart</a>
                {% if user.is_authenticated %}
                    <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
                    <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                        Logout
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300 mb-2">
                        Login
                    </a>
                    <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
                        Register
                    </a>
                {% endif %}
            </div>
        </div>
        <script>
            const btn = document.querySelector("button.mobile-menu-button");
            const menu = document.querySelector(".mobile-menu");

            btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
            });
        </script>
        <style>
            .text-gold { color: #d4af37; }
            .font-medieval { font-family: 'UnifrakturMaguntia', cursive; }
            .bg-gold { background-color: #d4af37; }
            .bg-gold-dark { background-color: #b8972b; }
            .border-gold { border-color: #d4af37; }
            .focus:ring-gold { --tw-ring-color: #d4af37; }
            .focus:border-gold { border-color: #d4af37; }
        </style>
    </nav>
    ```

    6. Menambahkan path untuk ke static folder pada settings.py
    STATIC_URL = '/static/'
    if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    else:
    STATIC_ROOT = BASE_DIR / 'static' 

    7. Memodifikasi tampilan
    mengubah register.html, main.html, edit_product.html, card_product.html, card_info.html, login.html, create_product_entry.html sesuai selera. Punya saya belum terlalu banyak berubah karena saya kekurangan imajinasi, nanti akan saya ubah lagi.

# Tugas 6

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web

    1. Interaktivitas: Memungkinkan halaman web menjadi lebih dinamis dan responsif terhadap interaksi pengguna.
    2. Client-Side Processing: Mengurangi beban server dengan melakukan proses di browser.
    3. AJAX: Mengirim dan menerima data dari server tanpa me-refresh halaman.
    4. Pengalaman Pengguna: Meningkatkan UI dengan elemen-elemen interaktif dan real-time.
    5. Integrasi dengan HTML/CSS: Memanipulasi elemen halaman secara langsung.
    6. Pengembangan Aplikasi Modern: Mendukung SPA dan PWA untuk pengalaman aplikasi seperti native.
    7. Ekosistem Besar: Banyak pustaka dan framework yang mendukung pengembangan lebih cepat.
    8. JavaScript memberikan kekuatan untuk membuat web lebih interaktif, cepat, dan fungsional.

    JavaScript memberikan kekuatan untuk membuat web lebih interaktif, cepat, dan fungsional.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

    Fungsi penggunaan await saat menggunakan fetch() adalah untuk menunggu sampai permintaan HTTP selesai dan responsnya diterima sebelum melanjutkan ke baris kode berikutnya. Dengan kata lain, await memastikan bahwa kode yang menunggu hasil dari fetch() ditangguhkan hingga permintaan selesai, sehingga kita dapat bekerja dengan hasil respons.

    Tanpa await, response hanya berupa promise, bukan data aktual yang diharapkan dari server, sehingga kita tidak dapat langsung menggunakannya tanpa memanggil .then() atau cara lain untuk menangani promise tersebut.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

    Kita perlu menggunakan decorator csrf_exempt pada view yang digunakan untuk AJAX POST karena secara default, Django memiliki mekanisme CSRF (Cross-Site Request Forgery) protection yang memerlukan token khusus untuk semua permintaan POST. CSRF adalah lapisan keamanan yang melindungi aplikasi dari serangan di mana permintaan dibuat dari sumber tidak sah ke server.

    Dalam konteks AJAX POST, jika CSRF token tidak dikirim bersama permintaan, Django akan memblokir permintaan tersebut karena dianggap tidak aman. Jika kita menggunakan csrf_exempt, Django tidak akan melakukan pemeriksaan CSRF pada view tersebut, memungkinkan AJAX POST untuk berjalan tanpa membutuhkan token CSRF.

    Jika kita tidak menggunakan csrf_exempt dan AJAX POST tidak mengirimkan CSRF token yang benar, Django akan memunculkan error 403 Forbidden. csrf_exempt dapat berguna dalam situasi tertentu, terutama untuk permintaan yang tidak membutuhkan CSRF protection (misalnya API endpoint publik atau pengujian).

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

    1. Keamanan: Pengguna bisa mem-bypass validasi di frontend, sehingga backend melindungi dari serangan seperti injection.
    2. Kontrol: Backend memastikan semua input sesuai aturan, tanpa bergantung pada kode di browser.
    3. Integritas Data: Semua data yang masuk ke sistem diperiksa secara konsisten.
    4. Mencegah Manipulasi: Pengguna bisa mematikan atau mengubah validasi di frontend.
    5. Multi-platform: Data bisa datang dari berbagai sumber selain frontend, sehingga backend harus selalu melakukan pembersihan.

    Backend melindungi aplikasi meski validasi di frontend dilewati.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Menggunakan AJAX `GET`, tambahkan di views.py
    ```python
    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):
        name = strip_tags(request.POST.get("name"))
        description = strip_tags(request.POST.get("description")) 
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        quantity = request.POST.get("quantity")
        user = request.user

        new_product = ProductEntry(
            name=name, description=description, 
            quantity=quantity, price=price,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    ```

    2. Tambahkan di `urls.py`
    ```python
    from main.views import add_product_entry_ajax
    urlpatterns = [
    ...
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    ]
    ```

    3. Di main.html, tambahkan fungsi get:
    ```python
    ...
    <div id="product_entry_cards"></div>
    ...

    <script>
    async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
    </script>
    ```

    dan refresh:

    ```python
    async function refreshProductEntries() {
        document.getElementById("product_entry_cards").innerHTML = "";
        document.getElementById("product_entry_cards").className = "";
        const productEntries = await getProductEntries();
        let htmlString = "";
        let classNameString = "";

        if (productEntries.length === 0) {
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
                <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                    <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                    <p class="text-center text-gray-600 mt-4">Belum ada data product pada Muljawan's Tavern.</p>
                </div>
            `;
        }
        else {
            classNameString = "columns-1 sm:columns-2 lg:columns-5 gap-6 space-y-6 w-full"
            productEntries.forEach((item) => {
                const name = DOMPurify.sanitize(item.fields.name);
                const description = DOMPurify.sanitize(item.fields.description);
                htmlString += `
                <div class="relative break-inside-avoid">
                <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                    <div class="w-[2rem] h-6 bg-brown-200 rounded-md opacity-80 -rotate-90"></div>
                    <div class="w-[2rem] h-6 bg-brown-200 rounded-md opacity-80 -rotate-90"></div>
                </div>

                <div class="relative top-5 bg-black bg-opacity-70 shadow-md rounded-lg mb-4 break-inside-avoid flex flex-col border-2 border-gold transform rotate-1 hover:rotate-0 transition-transform duration-300 max-w-xs">
                    <div class="bg-black bg-opacity-50 text-brown p-3 rounded-t-lg border-b-2 border-gold">
                    <h3 class="font-bold text-lg mb-1 text-gold bg-white p-1 px-2 rounded-full inline-block">${name}</h3>
                    </div>
                    <div class="p-3">
                    <p class="font-bold text-md mb-1 text-white">Price</p>
                    <p class="text-black-300 mb-1">
                        <span class="bg-white p-1 px-2 rounded-full inline-block">${item.fields.price}</span>
                    </p>

                    <p class="font-bold text-md mb-1 text-white">Description</p>
                    <p class="text-black-300 mb-1">
                        <span class="bg-white p-1 px-2 rounded-full inline-block">${description}</span>
                    </p>

                    <p class="font-bold text-md mb-1 text-white">Quantity</p>
                    <p class="text-black-300 mb-1">
                        <span class="bg-white p-1 px-2 rounded-full inline-block">${item.fields.quantity}</span>
                    </p>
                    </div>
                </div>

                <div class="absolute top-5 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex space-x-1">
                    <a href="/edit-product/${item.pk}" class="bg-gold hover:bg-gold-dark text-black rounded-full p-1 transition duration-300 shadow-md border-2 border-black">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                    </a>

                    <a href="/delete/${item.pk}" class="bg-red-700 hover:bg-red-800 text-white rounded-full p-1 transition duration-300 shadow-md border-2 border-black">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    </a>
                </div>
                </div>
                `;
            });
        }
        document.getElementById("product_entry_cards").className = classNameString;
        document.getElementById("product_entry_cards").innerHTML = htmlString;
    }
    refreshProductEntries();
    ```

    4. Di main.html, Implementasi modal sbg form, menambahkan fungsi yg berguna, dan button 
    ```python
    ...
    <div class="flex justify-center mb-6">
        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-gold hover:bg-dark-gold text-black font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-5" onclick="showModal();">
        Add New Product
        </button>
    </div>
    ...

    <script>
    ...
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
        modal.classList.add('hidden');
        }, 150); 
    }
    ...
    </script>
    ```

    5. Mengubah fitur menampilkan data product dengan AJAX `POST`, tambahkan fungsi baru agar modal form bekerja

    ```python
    <script>
    function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries())

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
    }
    ...

    document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProductEntry();
    })
    </script>
    ```

    6. Buka `views.py` dan `forms.py` tambahkan impor di kedua file

    ```python
    from django.utils.html import strip_tags
    ```

    7. bersihkan data untuk melindungi dari XSS, tambahakan fungsi di views.py

    ```python
    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):
        name = strip_tags(request.POST.get("name"))
        description = strip_tags(request.POST.get("description")) 
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        quantity = request.POST.get("quantity")
        user = request.user

        new_product = ProductEntry(
            name=name, description=description, 
            quantity=quantity, price=price,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    ```

    8. tambah method untuk membersihkan data di `forms.py`

    ```python
    class ProductEntryForm(ModelForm):
        class Meta:
            model = ProductEntry
            fields = ["name", "price", "description", "quantity"]
        
        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
    ```

    9. implementasi DOMPurifiy di main.html
    ```python
    ...
    productEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const description = DOMPurify.sanitize(item.fields.description);
    ...
    ```


