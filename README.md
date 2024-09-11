# muljawan-store

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
![](bagan/MVT Django.jpeg)

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