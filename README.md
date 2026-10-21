# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Dita Amalia Veronica
NIM: 2225250162
Kelas: 3F

## Tujuan

Mengolah kumpulan data numerik dengan list Python: membuat list, mengakses elemen (indeks dan slicing), memodifikasi elemen, menelusuri list dengan perulangan, menghitung statistik dasar (total, rata-rata, minimum, maksimum), dan menyusun fungsi yang menerima list sebagai parameter. Praktik inti berupa program analisis nilai mahasiswa dengan batas kelulusan 60.

## Struktur Program

```
pertemuan-09-list-NIM/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_buat_list.py
|   |-- 02_indeks_slicing.py
|   |-- 03_manipulasi_list.py
|   |-- 04_agregasi_nilai.py
|   |-- 05_filter_kelulusan.py
|   `-- 06_fungsi_statistik.py
`-- praktik/
    `-- analisis_nilai_mahasiswa.py
```

| File | Isi |
|------|-----|
| `01_buat_list.py` | Membuat list lima nilai, menampilkan list dan jumlah elemennya |
| `02_indeks_slicing.py` | Mengambil elemen pertama, terakhir, tiga elemen awal, dan indeks 1 sampai 3 |
| `03_manipulasi_list.py` | Mengubah, menambah (`append`), menyisipkan (`insert`), dan menghapus (`remove`) elemen |
| `04_agregasi_nilai.py` | Menghitung total, rata-rata, minimum, dan maksimum |
| `05_filter_kelulusan.py` | Menyaring nilai yang lulus (batas 60) dan menghitung jumlahnya |
| `06_fungsi_statistik.py` | Fungsi `rata_rata(data)` yang aman untuk list kosong |
| `praktik/analisis_nilai_mahasiswa.py` | Program analisis nilai 10 mahasiswa dengan dua fungsi: `rata_rata` dan `nilai_lulus` |

## Cara Menjalankan

```
python3 praktik/analisis_nilai_mahasiswa.py
```

Pada Windows, gunakan `python` sebagai ganti `python3`. Contoh output dengan data `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]`:

```
Data          : [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
Banyak data   : 10
Total         : 695
Rata-rata     : 69.50
Minimum       : 45
Maksimum      : 90
Nilai lulus   : [78, 90, 67, 60, 82, 71, 88]
Jumlah lulus  : 7
Belum lulus   : 3
```

## Algoritma

1. Siapkan list nilai (minimal 10 data).
2. Hitung banyak data dengan `len`.
3. Hitung total (`sum`), minimum (`min`), maksimum (`max`), dan rata-rata (`sum` dibagi `len`).
4. Telusuri setiap nilai dengan `for` dan periksa kelulusan dengan `if x >= batas`.
5. Tambahkan nilai yang lulus ke list baru dengan `append`.
6. Hitung jumlah belum lulus dari banyak data dikurangi jumlah lulus.
7. Tampilkan seluruh hasil dengan f-string.

Fungsi `rata_rata(data)` mengembalikan 0 jika list kosong, supaya tidak terjadi `ZeroDivisionError`. Fungsi `nilai_lulus(data, batas=60)` mengembalikan list nilai yang memenuhi batas kelulusan.

## Test Case

| No | Data | Yang Diperiksa | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|------|----------------|-----------------------|--------------|--------|
| 1 | `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Berhasil |
| 2 | `[60, 70, 80]` | Minimum / maksimum | 60 / 80 | 60 / 80 | Berhasil |
| 3 | `[60, 70, 80]` | Jumlah lulus | 3 | 3 | Berhasil |
| 4 | `[59, 60, 61]` | Batas kelulusan | 2 lulus | 2 lulus | Berhasil |
| 5 | `[]` | Penanganan list kosong pada fungsi rata-rata | Tidak error | Mengembalikan 0, tidak error | Berhasil |

Catatan test case nomor 4: nilai 59 tidak lulus, sedangkan 60 dan 61 lulus. Ini membuktikan batas kelulusan memakai `>=` (nilai 60 dihitung lulus).

## Refleksi

Satu hal yang saya pahami tentang indeks/list: indeks Python dimulai dari 0 dan indeks negatif menghitung dari belakang (`-1` adalah elemen terakhir). Pada slicing `nilai[1:4]`, indeks akhir tidak ikut diambil, jadi yang terambil adalah indeks 1, 2, dan 3.

Satu kesalahan yang berhasil diperbaiki: rata-rata dari list kosong akan menimbulkan `ZeroDivisionError` karena dibagi `len(data)` yang bernilai 0. Saya memperbaikinya dengan memeriksa `len(data) == 0` terlebih dahulu dan mengembalikan 0. Selain itu, saya belajar bahwa satu test case saja tidak cukup; data normal, nilai batas (60), dan list kosong perlu diuji.

## Sumber dan Bantuan

- Bahan Ajar Pertemuan 9 (Algoritma dan Pemrograman, Untirta, 2026/2027 Ganjil).
- Python 3 Documentation: Data Structures.
- Bantuan AI (Claude) digunakan untuk membantu menyusun README dan memeriksa hasil test case. Kode dan alasan pemilihan operasi list dapat saya jelaskan.