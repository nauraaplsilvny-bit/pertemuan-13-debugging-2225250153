# Pertemuan 13 - Debugging dan Testing

Nama: Naura Palisa Ievani
NIM: 2225250153
Kelas: 3F

## Kasus
Program yang diuji adalah program pengolahan data nilai mahasiswa.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report

1. Bug rata-rata:
   Program selalu membagi jumlah nilai dengan 5.
   Perbaikan menggunakan len(nilai).

2. Bug status:
   Operator > menyebabkan nilai 60 tidak lulus.
   Perbaikan menggunakan >=.

3. Bug nilai tertinggi:
   Operator < membuat pencarian nilai tertinggi salah.
   Perbaikan menggunakan >.

## Retest
Catat hasil pengujian setelah perbaikan.

## Cara Menjalankan
python3 praktik/praktik_4_debugging.py

## Refleksi
Teknik debugging yang paling membantu adalah tracing
karena dapat melihat perubahan nilai variabel secara bertahap.