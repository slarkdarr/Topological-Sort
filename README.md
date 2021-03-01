# Tugas Kecil 2 -- 13519107
## IF2211 -- Strategi Algoritma
### Penyusunan Rencana Kuliah dengan *Topological Sort*

## Deskripsi Singkat
Program melakukan *sorting* terhadap kumpulan mata kuliah yang dapat diambil pada tiap semester dengan menggunakan algoritma *Topological Search* dan pendekatan *Decrease and Conquer*.<br/>
a. Pertama, program akan melakukan *scan* terhadap file input dan mengubahnya menjadi list representasi graf (DAG).<br/>
b. Lalu, program akan mencari mata kuliah yang berupa simpul yang belum pernah diambil dan prasyaratnya telah terpenuhi (derajat masuk == 0).<br/>
c. Kemudian, program akan mengambil simpul tersebut serta menghapus simpul tersebut dari DAG beserta dengan semua sisi yang keluar dari simpul tersebut.<br/>
d. Setelah itu, program akan mengurangi derajat simpul yang berhubungan dengan simpul tersebut dengan 1.<br/>
e. Langkah (b), (c), dan (d) akan terus diulangi sampai semua simpul pada DAG terpilih atau dalam kata lain, DAG kosong.<br/>

## *Requirement* Program
<a href="https://www.python.org/downloads/" target="_blank">Python 3</a>
  
## Cara Menggunakan Program
1. Buka git bash<br/>
2. Ubah direktori ke tempat Anda ingin menyimpan file ini<br/>
3. Ketik `git clone https://github.com/slarkdarr/Tucil2_13519107.git`<br/>
4. Buka command prompt<br/>
5. Ubah direktori ke tempat dimana Anda telah menyimpan file yang telah di-*clone* sebelumnya menggunakan command `cd ...`<br/>
6. Ketik `python3 13519107.py` atau `python 13519107.py`<br/>
7. Program akan berjalan sesuai dengan input dari file teksnya<br/>
8. Untuk mengubah file teks yang digunakan, ubah variabel `filename` pada bagian program utama dengan nama file yang ingin digunakan<br/>

## Author / Identitas Pembuat
Nama  : Daffa Ananda Pratama Resyaly<br/>
NIM   : 13519107<br/>
Kelas : 02<br/>

 <a href="#top">Back to top</a>
