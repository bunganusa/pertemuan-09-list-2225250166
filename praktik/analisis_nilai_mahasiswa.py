def rata_rata(data):
    """Menghitung nilai rata-rata dari list data numerik."""
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    """Menyaring dan mengembalikan list nilai yang memenuhi batas kelulusan."""
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

def main():
    # Data sekumpulan nilai mahasiswa (10 data)
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    batas_kriteria = 60

    # Menghitung statistik dasar
    banyak_data = len(nilai)
    total_nilai = sum(nilai)
    mean = rata_rata(nilai)
    min_nilai = min(nilai) if banyak_data > 0 else 0
    max_nilai = max(nilai) if banyak_data > 0 else 0

    # Menyaring data kelulusan
    list_lulus = nilai_lulus(nilai, batas=batas_kriteria)
    jumlah_lulus = len(list_lulus)
    jumlah_belum_lulus = banyak_data - jumlah_lulus

    # Menampilkan ringkasan output
    print("=" * 45)
    print("      RINGKASAN ANALISIS NILAI MAHASISWA     ")
    print("=" * 45)
    print(f"Data Nilai         : {nilai}")
    print(f"Banyak Data        : {banyak_data}")
    print("-" * 45)
    print(f"Total Nilai        : {total_nilai}")
    print(f"Rata-rata Nilai    : {mean:.2f}")
    print(f"Nilai Minimum      : {min_nilai}")
    print(f"Nilai Maksimum     : {max_nilai}")
    print("-" * 45)
    print(f"Batas Kelulusan    : {batas_kriteria}")
    print(f"Daftar Nilai Lulus : {list_lulus}")
    print(f"Jumlah Lulus       : {jumlah_lulus}")
    print(f"Belum Lulus        : {jumlah_belum_lulus}")
    print("=" * 45)

if __name__ == "__main__":
    main()