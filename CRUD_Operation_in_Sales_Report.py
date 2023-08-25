# CAPSTONE MODUL 1

# Database menggunakan dictionary in dictionary 
# Untuk memudahkan pekerjaan dengan menggunakan kata kunci atau keys untuk mengakses itemnya
dataPembelian = {
    'IPK00001'  :{
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
                },
    'SBA00005'  :{
                'Nama Pembeli':'PT Selamanya Bersama',
                'Quantity': 250,
                'Metode Pembayaran':'Tunai',
                'Harga':60000,
                'Total Pembelian':15000000
                },
    'SPA00008'  :{
                'Nama Pembeli':'PT Setiawan Abadi',
                'Quantity': 180,
                'Metode Pembayaran':'Tunai',
                'Harga':60000,
                'Total Pembelian':10800000
                }
                }

# pada menu interface ditampilkan fitur fitur yang dapat digunakan pada program ini
# digunakan regular function yang berisi conditional statement untuk mengarahkan keprogram yang ingin digunakan

# Tampilan menu utama
def interface(): 
    print('''
        ======================================================
        ================== MENU UTAMA ========================
        ======================================================
        Selamat Datang di Menu Utama Laporan Penjualan
        1. Membuat Laporan Penjualan
        2. Menampilkan Laporan Penjualan
        3. Update Laporan Penjualan
        4. Menghapus Laporan Penjualan
        5. Exit Program
        ''')
    pilihan = input('Masukan pilihan anda:')                                     # menggunakan input untuk mengetahui fitur yang ingin digunakan oleh user
    if pilihan == '1': 
        membuat()
    elif pilihan == '2':
        menampilkan()
    elif pilihan == '3':
        update()
    elif pilihan == '4':
        menghapus()
    elif pilihan == '5':
        exit()
    else:
        print('Pilihan yang anda masukan tidak tersedia')  
        print()                                                                     # information box untuk memberitahu user agar 
        interface()                                                                 # memberikan input sesuai opsi yang tersedia

# Regular function untuk Create
def membuat():                                                           
    print('''
        ========================================================
        ----------------------- CREATE -------------------------
        ========================================================
        1. Membuat Data Laporan Penjualan Baru
        2. Menu Utama
        ========================================================
        ''')
    pilihanMembuat = input('masukan pilihan anda:')
    if pilihanMembuat == '1':
        POBaru = input('masukan nomor purchase baru yang akan anda buat:').upper()    # .upper digunakan untuk meminimalisir kesalahan user dalam menginput PO
        if POBaru in dataPembelian.keys():                                          # karena terdapat persyaratan yaitu untuk PO harus terdiri dari huruf capital
            # Melakukan pengecekan untuk keys yang akan dimasukan untuk menghindari duplicate
            print('Nomor Purchase Order sudah ada sebelumnya')
            print()
            membuat()
        else:                                                                       # user melakukan input untuk setiap itemnya
            NPBaru = input('masukan nama pembeli:').capitalize()
            quantityBaru = int(input('masukan kuantitas pembelian:'))
            MPBaru = input('masukan metode pembayaran:').capitalize()
            hargaBaru = int(input('masukan harga pembelian:'))
            TPBaru = quantityBaru*hargaBaru
            dataPembelian.update({                                                  # update terhadap data yang baru dimasukan dengan function .update
                (POBaru)    :{
                            'Nama Pembeli':(NPBaru),
                            'Quantity': (quantityBaru),
                            'Metode Pembayaran':(MPBaru),
                            'Harga':(hargaBaru),
                            'Total Pembelian':(TPBaru)
                            }
                            })
            print(dataPembelian[POBaru])
            print()                                                                 # program akan melakukan konfirmasi ulang terkait penyimpanan data
            print('''                                                               
            ==========================================
            Apakah anda ingin menyimpan data tersebut?
            ==========================================
            1. YA
            2. TIDAK
            ------------------------------------------
            ''')
            pilihanSimpan = input('masukan pilihan anda:')
            if pilihanSimpan== '1':
                # Information box bahwa data telah tersimpan
                print(f'Laporan pembelian {dataPembelian[POBaru]["Nama Pembeli"]} telah tersimpan')
                interface()
            elif pilihanSimpan == '2':
                dataPembelian.pop(POBaru)                                           # function .pop untuk menghapus data yang telah dimasukan kedalam datapembelian
                membuat()
            else:
                print('pilihan yang anda masukan tidak tersedia')
                print()
                membuat()
    elif pilihanMembuat == '2':
        interface()
    else:
        print('Pilihan yang anda masukan tidak tersedia')
        print()
        membuat()

# Regular function untuk Read
def menampilkan():                                                                   
    print('''
        ========================================================
        ---------------------- READ ----------------------------
        ========================================================
        1. Menampilkan Data Penjualan Toko Keseluruhan
        2. Mencari Data Penjualan
        3. Menu Utama
        ========================================================
        ''')
    pilihanMenampilkan = input('masukan pilihan anda:')                               
    if pilihanMenampilkan == '1':
        print('Purchase Order\t|Nama Pembeli\t\t|Qty\t|Metode Pembayaran\t|Harga\t|Total Pembelian')
        for i in dataPembelian:                  
             # function for digunakan untuk proses looping print untuk menampilkan setiap data dalam datapembelian
            print(f'{i}\t|{dataPembelian[i]["Nama Pembeli"]}\t|{dataPembelian[i]["Quantity"]}\t|{dataPembelian[i]["Metode Pembayaran"]}\t\t\t|{dataPembelian[i]["Harga"]}\t|{dataPembelian[i]["Total Pembelian"]}')
        menampilkan()
    elif pilihanMenampilkan =='2':
        cariPO = input('Masukan Kode Purchase Order:')
        cariPOCaps = cariPO.upper()
        if cariPOCaps in dataPembelian:
            print(dataPembelian[cariPOCaps])
            print()
            menampilkan()
        else:
            print('Nomor purchase order yang anda masukan tidak tersedia')
            print()
            menampilkan()
    elif pilihanMenampilkan =='3':
        interface()
    else:
        print('Pilihan yang anda masukan tidak tersedia')
        menampilkan()

# Regular function untuk update
def update():                                                                           
    print('''
        ========================================================
        ----------------------- UPDATE -------------------------
        ========================================================
        1. Memperbarui Data Laporan Penjualan
        2. Menu Utama
        ========================================================
        ''')
    pilihanUpdate = input('Masukan pilihan anda:')
    if pilihanUpdate == '1':
        POUpdate = input('Masukan Purchase Order yang ingin diperbarui:').upper()
        if POUpdate in dataPembelian:
            print('''
            ------- Pilih Atribut Yang Ingin diperbarui -----------
            1. Nama Pembeli
            2. Quantity
            3. Metode Pembayaran
            4. Harga
            5. Total Pembelian
            ========================================================
            ''')

            pilihAtribut = input('masukan nomor atribut yang akan dipilih:')    # untuk meminimalisir human error ketika memasukan input
                                                                                # pilihan yang disediakan didefine terlebih dahulu didalam conditional statement
            if pilihAtribut == '1':
                atributUpdate = 'Nama Pembeli'
            elif pilihAtribut == '2':
                atributUpdate = 'Quantity'
            elif pilihAtribut == '3':
                atributUpdate = 'Metode Pembayaran'
            elif pilihAtribut =='4':
                atributUpdate = 'Harga'
            elif pilihAtribut == '5':
                atributUpdate = 'Total Pembelian'
            else:
                print('pilihan yang anda masukan tidak tersedia')
                update()

            atributBaru = input(f'masukan {atributUpdate} yang terbaru:').title() # penggunaan .title untuk menyesuaikan format penulisan dengan item di database
            print('''
            ========================================================
            ---Apakah Anda Yakin Ingin Memperbarui Data Tersebut?---
            ========================================================
            1. YA
            2. TIDAK
            ========================================================
            ''')
            konfirmasiUpdate = input('masukan pilihan anda:')
            if konfirmasiUpdate == '1':
                dataPembelian[POUpdate][atributUpdate]= atributBaru
                print(dataPembelian[POUpdate])
                print()
                print('data telah diperbarui')
                update()
            elif konfirmasiUpdate == '2':
                update()
            else:
                print('pilihan yang anda masukan tidak tersedia')
                print()
                update()
        else:
            print('Nomor purchase order yang anda masukan tidak tersedia')
            print()
            update()
    elif pilihanUpdate == '2':
        interface()
    else:
        print('Pilihan yang anda masukan tidak tersedia')
        update()

def menghapus():
    print('''
        ========================================================
        --------------------- DELETE ---------------------------
        ========================================================
        1. Menghapus Data Laporan Penjualan
        2. Menu Utama
        ========================================================
        ''')
    pilihanHapus = input('Masukan pilihan anda:')
    if pilihanHapus == '1':
        POHapus = input('Masukan Nomor Purchase Order Yang Ingin Anda Hapus:').upper()
        if POHapus in dataPembelian:
            print(dataPembelian[POHapus])
            print('''
                ========================================================
                ------- Apakah Anda Ingin Menghapus Laporan ini? -------
                ========================================================
                1. Ya
                2. Tidak
                ========================================================
                ''')
            konfirmasiHapus = input('masukan pilihan anda:')
            if konfirmasiHapus == '1':
                dataPembelian.pop(POHapus)
                print('Laporan penjualan tersebut telah dihapus')
                menghapus()
            elif konfirmasiHapus == '2':
                menghapus()
            else:
                print('pilihan yang anda masukan tidak tersedia')
                print()
                menghapus()
        else:
            print('Nomor purchase order yang anda masukan tidak tersedia')
            print()
            menghapus()
    elif pilihanHapus == '2':
        interface()
    else:
        print('Pilihan yang anda masukan tidak tersedia')
        print()
        menghapus()

# Regular function untuk exit
def exit():
    print('''
        =======================================
        Apakah anda ingin meninggalkan program?
        =======================================
        1. YA
        2. TIDAK
        ---------------------------------------
        ''')
    pilihanExit = input('masukan pilihan anda:')
    if pilihanExit == '1':
        print('Terima Kasih!')
    elif pilihanExit == '2':
        interface()
    else:
        print('pilihan anda tidak tersedia')
        print()
        interface()

interface()