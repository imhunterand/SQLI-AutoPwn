# SQLI-AutoPwn

## Deskripsi

SQLI-AutoPwn adalah alat otomatis untuk mendeteksi dan mengeksploitasi celah SQL Injection pada aplikasi web. Alat ini dirancang untuk mengidentifikasi parameter input yang rentan terhadap SQL Injection, mengeksploitasi celah tersebut menggunakan serangkaian payload, dan memberikan akses ke basis data target. Alat ini juga memungkinkan pengguna untuk melakukan berbagai operasi pada basis data yang diambil alih, seperti enumerasi tabel, ekstraksi data, dan eksekusi perintah SQL.

## Fitur Utama

1. **Deteksi Otomatis SQL Injection:**
   - Mengidentifikasi parameter input yang rentan terhadap SQL Injection.

2. **Eksploitasi Celah SQL Injection:**
   - Menggunakan serangkaian payload untuk mengeksploitasi celah SQL Injection.

3. **Pengambilalihan Basis Data:**
   - Memberikan akses ke basis data target dan memungkinkan eksekusi perintah SQL.

4. **Enumerasi Tabel dan Kolom:**
   - Memungkinkan pengguna untuk mengekstrak informasi tentang tabel dan kolom dalam basis data.

5. **Ekstraksi Data:**
   - Memungkinkan pengguna untuk mengekstrak data dari tabel yang diambil alih.

## Langkah-langkah Penggunaan

### 1. Inisialisasi Proyek

Buat direktori proyek dan instal dependensi yang diperlukan.

```sh
mkdir sqli_autopwn
cd sqli_autopwn
touch requirements.txt
echo "requests\nsqlalchemy" > requirements.txt
pip install -r requirements.txt
```

### 2. Menjalankan Skrip Deteksi SQL Injection
Gunakan skrip `sqli_detector.py` untuk mendeteksi parameter yang rentan terhadap SQL Injection.

### 3. Eksploitasi dan Pengambilalihan Basis Data
Gunakan skrip sqli_exploit.py untuk mengeksploitasi celah dan mengambil alih basis data target.

### 4. Operasi pada Basis Data yang Diambil Alih
Skrip akan mencetak tabel, kolom, dan data dari basis data yang diambil alih.

```
sqli_autopwn/
│
├── requirements.txt
├── sqli_detector.py
└── sqli_exploit.py
```

