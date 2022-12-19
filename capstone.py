data = {
    1: ['Gula', 'Kotak 250 g', 'Bahan Masakan',3, 8000], 
    2: ['Bakso Goreng', 'Pouch 100 g', 'Makanan Kemasan',12, 1000], 
    3: ['Teh Cair', 'Kotak 200 ml', 'Minuman Kemasan',23, 4000], 
    4: ['Kopi', 'Pouch 200 g', 'Minuman Kemasan',4, 15000], 
    5: ['Bawang', 'Pouch 3 Ons', 'Bahan Masakan',10, 25000],
    6: ['Susu Bubuk', 'Pouch 300 g', 'Minuman Kemasan',3, 3000], 

}  

kode_karyawan = [1132,1234,6678,1112,8897]

def header_table():
    print('No. | Nama Barang          | Ukuran                | Kategori            | QTY    | Harga/Unit           |')
    print('---------------------------------------------------------------------------------------------------------')

def main_menu():
    while(True):
        print("======Masuk Sebagai======\n")
        print("=========================")
        print("1. Karyawan")
        print("2. Pembeli")
        print("3. Exit Program")
        print("=========================\n\n")

        pilihan = int(input("Masukkan Pilihan  : "))
        if(pilihan == 1):
            login()
        elif(pilihan == 2):
            customer_menu()
        elif(pilihan == 3):
            quit()
        else:
            print("===Pilihan Tidak Ada===")
            


def customer_menu():
    while(True):
        print("===Halo Selamat Datang di Warung===\n\n")
        print("Pilih Menu\n")
        print("=========================")
        print("1. Tampilkan Stok")
        print("2. Belanja")
        print("3. Main Menu")
        print("=========================\n\n")

        
        pilihan = int(input("Masukkan pilihan : "))
        if(pilihan == 1):
            read_all()
        elif(pilihan == 2):
            belanja()
        elif(pilihan == 3):
            main_menu()
        else:
            print("Pilihan Tidak Ada")

def karyawan_menu():
    while(True):
        print("===Program Stok Warung===\n\n")
        print("Pilih Menu\n")
        print("=========================")
        print("1. Tampilkan Barang")
        print("2. Tambah Data Barang")
        print("3. Update Barang")
        print("4. Delete Barang")
        print("5. Kembali ke Main Menu")
        print("=========================\n\n")

        pilihan = int(input("Masukkan Pilihan  : "))
        if(pilihan == 1):
            read_menu_karyawan()
        elif(pilihan == 2):
            add_menu_karyawan()
        elif(pilihan == 3):
            update_menu_karyawan()
        elif(pilihan == 4):
            delete_menu_karyawan()
        elif(pilihan == 5):
            main_menu()
        else:
            print("===Pilihan Tidak Ada===")
        

def read_menu_karyawan():
    print("===Stok Menu===\n\n")
    print("Pilih Menu\n")
    print("=========================")
    print("1. Tampilkan Per Kategori")
    print("2. Tampilkan Semua")
    print("3. Cari dengan Keyword")
    print("4. Kembali ke Main Menu")
    print("=========================\n\n")

    pilihan = int(input("Masukkan Pilihan  : "))
    if(pilihan == 1):
        read_by_kategori()
    elif(pilihan == 2):
        read_all_stock()
    elif(pilihan == 3):
        read_by_keyword()
    elif(pilihan == 4):
        karyawan_menu()

    else:
        print("===Pilihan Tidak Ada===")
        karyawan_menu()



def update_menu_karyawan():
    read_all()

    temp_check = input("Masukkan Nama Barang yang ingin diupdate: ")
    print(temp_check)
    index = None
    for key, value in data.items():
        if value[0].lower() == temp_check.lower():
            index = key
            break

    if index:
        print(temp_check, "Ada di nomor ", index)
    else:
        print('Barang tidak ditemukan')
        
    print("===Update Barang===\n\n")
    print("Pilih Field yang ingin diubah dari barang ", temp_check, "\n")
    print("=========================")
    print("1. Nama Barang")
    print("2. Ukuran")
    print("3. Kategori")
    print("4. QTY")
    print("5. Harga/Unit")
    print("6. Batal Update, Kembali Ke Menu Karyawan")
    print("=========================\n\n")

    pilihan = int(input("Masukkan Pilihan : "))
    if(pilihan < 4 ):
        new_value = input("Masukkan Value Terbaru : ")
    elif(pilihan >= 4 and pilihan <=5):
        new_value = int(input("Masukkan Value Terbaru : "))
    elif(pilihan == 6):
        karyawan_menu()
    else:
        print("Pilihan Tidak Ada")
        karyawan_menu()
    
    
    print(type(new_value))
    update_data(index,pilihan - 1,new_value)
    read_all()

    karyawan_menu()

def update_data(idx1, idx2, value):
    
    data[idx1][idx2] = value 

def delete_menu_karyawan():
    for i, item in data.items():
        print(f"{i}: {item[0]}")
    
    pilihan = int(input("Masukkan Nomor dari nama barang yang ingin anda hapus : "))
    while(True):
        setuju = input("Yaklin ingin mehgapus data ini ? (y/n) : ")
        if(setuju.lower() == 'y'):
            del data[pilihan]
            read_all()
            break
        elif(setuju.lower() == 'n'):
            break
        else:
            print("Pilihan Tidak Ada, Coba lagi")

    karyawan_menu()

def login():
    kode = int(input("Masukkan kode karyawan : "))

    for i in kode_karyawan:
        if i == kode:
            karyawan_menu()
    
    print("====[KODE SALAH]====\n")
    main_menu()

def read_all():
    header_table()

    # Cetak baris tabel menggunakan perulangan
    for i in data:
        nama = data[i][0]
        ukuran = data[i][1]
        kategori = data[i][2]
        jumlah = data[i][3]
        harga = data[i][4]

        # Menggunakan string formatting untuk mencetak baris tabel dengan format yang diinginkan
        print(f'{i:3} | {nama:20} | {ukuran:20} | {kategori:20} | {jumlah:6} | {harga:20} |')
def read_all_stock():
    read_all()

    read_menu_karyawan()
def read_by_kategori():
    print("=========================\n")
    # Buat set kategori untuk menyimpan kategori yang unik
    temp_kategori = set()
    
    # Tambahkan kategori ke set menggunakan perulangan
    for i in data:
        kategori = data[i][2]
        temp_kategori.add(kategori)

    kategoriSet = list(temp_kategori)

    # Cetak set kategori
    for i in range(len(temp_kategori)):
        print(i + 1, kategoriSet[i])

    print("=========================\n")

    pilihan = int(input("Masukkan Pilihan : "))
    pilihan = kategoriSet[pilihan-1]

    header_table()

    # Cetak baris tabel menggunakan perulangan
    for i in data:
        nama = data[i][0]
        ukuran = data[i][1]
        kategori = data[i][2]
        jumlah = data[i][3]
        harga = data[i][4]
        if(pilihan == kategori):
        # Menggunakan string formatting untuk mencetak baris tabel dengan format yang diinginkan
            print(f'{i:3} | {nama:20} | {ukuran:20} | {kategori:20} | {jumlah:6} | {harga:20} |')

    read_menu_karyawan()

def read_by_keyword():
    read_all()

    keyword = input("Masukkan Keyword dengan Primary Key [Nama Barang] :")
    keyword = keyword.lower()
    header_table()
    for i in data:
        nama = data[i][0]
        ukuran = data[i][1]
        kategori = data[i][2]
        jumlah = data[i][3]
        harga = data[i][4]

        
        if keyword in nama.lower():
            # Menggunakan string formatting untuk mencetak baris tabel dengan format yang diinginkan
            print(f'{i:3} | {nama:20} | {ukuran:20} | {kategori:20} | {jumlah:6} | {harga:20} |')


    
    read_menu_karyawan()

def add_menu_karyawan():

    read_all()
    data_baru = []
    temp_check = input("Masukkan Nama Barang : ")
    
    for i in data:
        nama = data[i][0]

        
        if temp_check.lower() in nama.lower():
            print("Barang Sudah Ada !!!")
            karyawan_menu()
        else:
            
            temp_ukuran = input("Masukkan Ukuran Barang : ")
            temp_kategori = input("Masukkan kategori Barang : ")
            jumlah = int(input("Masukkan jumlah Barang : "))
            harga = int(input("Masukkan harga Barang : "))

            ukuran = temp_ukuran.title()
            check = temp_check.title()
            kategori = temp_kategori.title()
            data_baru.append(check)
            data_baru.append(ukuran)
            data_baru.append(kategori)
            data_baru.append(jumlah)
            data_baru.append(harga)
            data[len(data)+1] = data_baru
            read_all()
            karyawan_menu()
def belanja():
    
    read_all()
    keranjang = {}
    total_harga = 0
    

    while True:
        print("\nMenu:")
        for k, v in data.items():
            print(f"{k}. {v[0]} ({v[1]})")
        pilihan = input("\nMasukkan pilihan Anda (tekan b untuk bayar): ")
        if pilihan.lower() == 'b':
            bayar(total_harga, keranjang)
            break
        elif(int(pilihan) <= len(data)):
            
            jumlah = int(input("Masukkan jumlah: "))
            if(jumlah <= data[int(pilihan)][3]):


                nama_barang = data[int(pilihan)][0]
                harga_satuan = data[int(pilihan)][4]
                harga_total = harga_satuan * jumlah

                if nama_barang in keranjang:
                    keranjang[nama_barang]["jumlah"] += jumlah
                    keranjang[nama_barang]["harga_total"] += harga_total
                else:
                    keranjang[nama_barang] = {"jumlah": jumlah, "harga_satuan": harga_satuan, "harga_total": harga_total}

                total_harga += harga_total

                print("\nKeranjang Belanja:")
                for k, v in keranjang.items():
                    print(f"{k}: {v['jumlah']} x {v['harga_satuan']} = {v['harga_total']}")
                print(f"Total harga: {total_harga}")

            else:
                print("Stok kurang")



def bayar(total_harga,keranjang):
     
    kembalian = 0
    print("\nKeranjang Belanja:")
    for k, v in keranjang.items():
        print(f"{k}: {v['jumlah']} x {v['harga_satuan']} = {v['harga_total']}")
    print(f"Total harga: {total_harga}")
        
    uang_bayar = int(input("masukkan jumlah uang anda : "))
    if(total_harga<=uang_bayar):
        kembalian = uang_bayar - total_harga
            
    else:
        print("Uang anda kurang")
        bayar(total_harga,keranjang)
    print("Uang Kembalian : ", kembalian)
    for key, value in keranjang.items():
        # Ambil nama produk dari keranjang
        nama_produk = key
        # Ambil jumlah produk dari keranjang
        jumlah_produk = value['jumlah']

        # Cari produk dengan nama yang sesuai di data
        for k, v in data.items():
            if v[0] == nama_produk:
                # Kurangi stok produk di data dengan jumlah produk yang ada di keranjang
                data[k][3] -= jumlah_produk


   


        
    read_all()
    customer_menu()

if __name__ == "__main__":
    main_menu()