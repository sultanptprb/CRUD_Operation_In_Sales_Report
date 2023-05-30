# CRUD_Operation_In_Sales_Report

CRUD atau biasa dikenal dengan Create, Read, Update, Delete merupakan operasi sederhana yang sering digunakan
dalam suatu pemrograman dasar. Dalam masing-masing bahasa pemrograman sangat beragam cara pembuatannya, tetapi
sebenarnya konsepnya sama. Pada program demo sederhana ini akan melakukan operasi CRUD terhadap suatu laporan penjualan perusahaan. Tipe
Data yang digunakan adalah dictionary in dictionary dengan harapan dapat mempermudah pembuatan untuk menggunakan keys
agar dapat mengakses kedalam item data yang dibutuhkan.

Didalam program ini user dapat melakukan pembuatan laporan penjualan (Create), melihat semua data yang tersimpan didalam database (Read),
memperbarui data yang sudah ada sebelumnya didalam database (Update), dan menghapus data yang ada didalam database (Delete).
Berikut merupakan beberapa rincian dari program ini:

### Sample Data
```
    {'IPK00001'  :{
                'Nama Pembeli':'PT Indo Purna Karya',
                'Quantity': 120,
                'Metode Pembayaran':'Tunai',
                'Harga':60000,
                'Total Pembelian':7200000
                },
    'MSA00021'  :{
                'Nama Pembeli':'PT Maju Sejahtera',
                'Quantity': 390,
                'Metode Pembayaran':'Kredit',
                'Harga':60000,
                'Total Pembelian':23400000
                }}
```

### Main Interface
pada interface ini akan ditampilkan fitur atau function apa saja yang dapat digunakan oleh user dalam mengakses data
```
        ======================================================
        ================== MENU UTAMA ========================
        ======================================================
        Selamat Datang di Menu Utama Laporan Penjualan
        1. Membuat Laporan Penjualan
        2. Menampilkan Laporan Penjualan
        3. Update Laporan Penjualan
        4. Menghapus Laporan Penjualan
        5. Exit Program
```
### Create Interface
User dapat menambahkan laporan penjualan terbaru kedalam database dengan memasukan item-item yang dibutuhkan
```
	========================================================
        ----------------------- Menu 1 -------------------------
        ========================================================
        1. Membuat Data Laporan Penjualan Baru
        2. Menu Utama
        ========================================================
```
### Read Interface
User dapat melihat keseluruhan data yang terdapat didalam database, serta mencari data berdasarkan kata kuncinya.
```
        ========================================================
        --------------------- Menu 2 ---------------------------
        ========================================================
        1. Menampilkan Data Penjualan Toko Keseluruhan
        2. Mencari Data Penjualan
        3. Menu Utama
        ========================================================
```

### Update Interface
User dapat melakukan pembaruan terhadap data sebelumnya yang telah tersimpan didalam database
```
        ========================================================
        ----------------------- Menu 3 -------------------------
        ========================================================
        1. Memperbarui Data Laporan Penjualan
        2. Menu Utama
        ========================================================
```

# Delete Interface
User dapat menghapus laporan penjualan yang terdapat didalam database
```
        ========================================================
        --------------------- Menu 4 ---------------------------
        ========================================================
        1. Menghapus Data Laporan Penjualan
        2. Menu Utama
        ========================================================
```
