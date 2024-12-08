
# Membuat Database
database = [
    {'Kode Barang': 'A1', 'Nama Produk': 'So Klin', 'Kategori': 'Fabric Care', 'Stok': 300, 'Harga': 2000},
    {'Kode Barang': 'A2', 'Nama Produk': 'Nuvo', 'Kategori': 'Personal Care', 'Stok': 400, 'Harga': 3000},
    {'Kode Barang': 'A3', 'Nama Produk': 'Zinc', 'Kategori': 'Personal Care', 'Stok': 500, 'Harga': 1000},
    {'Kode Barang': 'A4', 'Nama Produk': 'Mie Sedaap', 'Kategori': 'Food', 'Stok': 1500, 'Harga': 3000},
    {'Kode Barang': 'A5', 'Nama Produk': 'Isoplus', 'Kategori': 'Food', 'Stok': 700, 'Harga': 3000},
    {'Kode Barang': 'A6', 'Nama Produk': 'Floridina', 'Kategori': 'Food', 'Stok': 500, 'Harga': 3000},
    {'Kode Barang': 'A7', 'Nama Produk': 'Daia', 'Kategori': 'Fabric Care', 'Stok': 1000, 'Harga': 1000},
    {'Kode Barang': 'A8', 'Nama Produk': 'Kodomo', 'Kategori': 'Personal Care', 'Stok': 300, 'Harga': 3000},
    {'Kode Barang': 'A9', 'Nama Produk': 'Guri Bee', 'Kategori': 'Food', 'Stok': 400, 'Harga': 5000},
    {'Kode Barang': 'A10', 'Nama Produk': 'Ciptadent', 'Kategori': 'Personal Care', 'Stok': 500, 'Harga': 3000},
]

from tabulate import tabulate
# Read Data
def read_data(data):
    print(tabulate(data, headers='keys', tablefmt='pretty'))


# Validate Input
def validate_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)

import re
# Validation Functions
def validate_kode_barang(kode):
    if not re.match(r'^[A-Z]\d*$', kode):
        return False
    for item in database:
        if item['Kode Barang'] == kode:
            return False
    return True

def validate_nama_produk(nama):
    return bool(re.match(r'^[A-Z][a-zA-Z\s\d]*$', nama))

def validate_kategori(kategori):
    return kategori in ['1', '2', '3']

def validate_stok(stok):
    try:
        int(stok)
        return True
    except ValueError:
        return False

def validate_harga(harga):
    try:
        int(harga)
        return True
    except ValueError:
        return False

# Create Data
def create_data():
    global database
    print('Data yang tersedia:')
    read_data(database)
    kodeBarang = validate_input('Masukkan Kode Barang: ', validate_kode_barang, 'Input harus berupa satu huruf besar dan dilanjutkan dengan angka, dan tidak boleh sama dengan kode barang yang sudah ada')
    namaProduk = validate_input('Masukkan Nama Produk: ', validate_nama_produk, 'Input harus diawali dengan huruf besar')
    kategori_input = validate_input('Pilih Kategori (1: Fabric Care, 2: Personal Care, 3: Food): ', validate_kategori, 'Input tidak valid')
    kategori_dict = {'1': 'Fabric Care', '2': 'Personal Care', '3': 'Food'}
    kategori = kategori_dict[kategori_input]
    stok = validate_input('Masukkan Jumlah Stok: ', validate_stok, 'Input Harus Angka')
    harga = validate_input('Masukkan Harga Barang: ', validate_harga, 'Input Harus Angka Bulat')
    data_baru = {'Kode Barang': kodeBarang, 'Nama Produk': namaProduk, 'Kategori': kategori, 'Stok': stok, 'Harga': harga}
    database.append(data_baru)
    print('Data berhasil ditambahkan')
    read_data(database)

# Update Data
def update_data():
    global database
    while True:
        print('Data yang tersedia:')
        read_data(database)
        kodeBarang = input('Masukkan Kode Barang yang ingin diupdate: ')
        item_found = False  # Mengecek apakah item ditemukan
        for item in database:
            if item['Kode Barang'] == kodeBarang:
                item_found = True
                print(f"Data lama: {item}")
                while True:
                    print('''
                    Pilih kolom yang ingin di-update:
                    1. Nama Produk
                    2. Kategori
                    3. Stok
                    4. Harga
                    ''')
                    pilihan = input('Masukkan pilihan (1/2/3/4): ')
                    if pilihan == '1':
                        item['Nama Produk'] = validate_input('Masukkan Nama Produk baru: ', validate_nama_produk, 'Input harus diawali dengan huruf besar')
                        break
                    elif pilihan == '2':
                        kategori_input = validate_input('Pilih Kategori baru (1: Fabric Care, 2: Personal Care, 3: Food): ', validate_kategori, 'Input tidak valid')
                        kategori_dict = {'1': 'Fabric Care', '2': 'Personal Care', '3': 'Food'}
                        item['Kategori'] = kategori_dict[kategori_input]
                        break
                    elif pilihan == '3':
                        item['Stok'] = validate_input('Masukkan Jumlah Stok baru: ', validate_stok, 'Input Harus Angka')
                        break
                    elif pilihan == '4':
                        item['Harga'] = validate_input('Masukkan Harga Barang baru: ', validate_harga, 'Input Harus Angka Bulat')
                        break
                    else:
                        print('Pilihan tidak valid, coba lagi.')
                print(f"Data baru: {item}")
                read_data(database)
                return
        if not item_found:
            print('Kode yang diinput tidak ditemukan, coba lagi.')


# Delete Data
def delete_data():
    global database
    while True:
        print('Data yang tersedia:')
        read_data(database)
        kodeBarang = input('Masukkan Kode Barang yang ingin dihapus: ')
        item_found = False  # Mengecek apakah item ditemukan
        for item in database:
            if item['Kode Barang'] == kodeBarang:
                item_found = True
                konfirmasi = input(f'Apakah Anda yakin ingin menghapus data dengan kode barang {kodeBarang}? (y/n): ')
                if konfirmasi.lower() == 'y':
                    database = [item for item in database if item['Kode Barang'] != kodeBarang]
                    print(f'Data dengan kode barang {kodeBarang} telah dihapus')
                    read_data(database)
                else:
                    print('Penghapusan data dibatalkan.')
                return
        if not item_found:
            print('Kode yang diinput tidak ditemukan, coba lagi.')

# Filter Data
def filter_data():
    while True:
        pilihan = input('Filter berdasarkan (1) Kategori atau (2) Nama Produk? ')
        if pilihan == '1':
            while True:
                print('''
                Pilih Kategori:
                1. Fabric Care
                2. Personal Care
                3. Food
                ''')
                kategori_input = input('Masukkan pilihan (1/2/3): ')
                kategori_dict = {'1': 'Fabric Care', '2': 'Personal Care', '3': 'Food'}
                kategori = kategori_dict.get(kategori_input, None)
                if kategori:
                    hasil_filter = [item for item in database if item['Kategori'] == kategori]
                    break
                else:
                    print('Pilihan kategori tidak valid, coba lagi.')

        elif pilihan == '2':
            produk_names = [item['Nama Produk'] for item in database]
            produk_names_lower = [name.lower() for name in produk_names]  
            while True:
                print('Daftar Nama Produk:')
                for idx, produk in enumerate(produk_names, 1):
                    print(f"{idx}. {produk}")
                namaProduk_input = input('Masukkan pilihan berdasarkan nomor atau nama produk: ').lower()  
                if namaProduk_input.isdigit():
                    idx = int(namaProduk_input) - 1
                    if 0 <= idx < len(produk_names):
                        namaProduk = produk_names[idx]
                        break
                    else:
                        print('Pilihan tidak valid, coba lagi.')
                elif namaProduk_input in produk_names_lower:
                    namaProduk = produk_names[produk_names_lower.index(namaProduk_input)]
                    break
                else:
                    print('Pilihan tidak valid, coba lagi.')

            hasil_filter = [item for item in database if namaProduk.lower() in item['Nama Produk'].lower()]
        else:
            print('Pilihan tidak valid, coba lagi.')
            continue

        if hasil_filter:
            read_data(hasil_filter)
        else:
            print('Tidak ada data yang sesuai')
        return

# Sort Data Berdasarkan Stok Terkecil dan Terbesar
def sort_data():
    while True:
        pilihan = input('Sort berdasarkan (1) Stok Terkecil atau (2) Stok Terbesar? ')
        if pilihan == '1':
            sorted_data = sorted(database, key=lambda x: x['Stok'])
            read_data(sorted_data)
            return
        elif pilihan == '2':
            sorted_data = sorted(database, key=lambda x: x['Stok'], reverse=True)
            read_data(sorted_data)
            return
        else:
            print('Pilihan tidak valid. Silakan pilih antara 1 atau 2.')

# Main (Utama)
def main():
    while True:
        print('''
        BERIKUT DATA STOK GUDANG TOKO X

        1. Read Data
        2. Create Data
        3. Update Data
        4. Delete Data
        5. Filter Data
        6. Sort Data Berdasarkan Stok
        7. Exit
        ''')

        inputan = input('Masukkan Menu: ')
        if inputan == '1':
            read_data(database)
        elif inputan == '2':
            create_data()
        elif inputan == '3':
            update_data()
        elif inputan == '4':
            delete_data()
        elif inputan == '5':
            filter_data()
        elif inputan == '6':
            sort_data()
        elif inputan == '7':
            break
        else:
            print('Menu tidak tersedia')

main()