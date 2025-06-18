import psycopg2
import pandas as pd 
import os
from datetime import datetime
from datetime import date

def header(isi=''):
    os.system('cls')
    print("───────────────────────────────────────────────────────────────")
    print("|                 < KLINIK INDONESIA SEHAT >                  |")
    print("───────────────────────────────────────────────────────────────")
    print("|    Jl. KH. Abdurrahman No.6, Tempurejo, Kec. Tempurejo,     |")
    print("|             Kabupaten Jember, Jawa Timur 68173              |")
    print("───────────────────────────────────────────────────────────────")
    print(" "*int((63-len(isi))/2)+isi)
    print("───────────────────────────────────────────────────────────────")

def connectDB():
    try:
        conn = psycopg2.connect(host="localhost", user="postgres", password="kamelia24", dbname="klinik")
        cur = conn.cursor()
        return conn, cur
    except Exception:
        return None

#--------------------------------------------------------------------------------------------------

def addPasien(email, user_password, nama, alamat, tanggal_lahir, no_telp, jenis_kelamin):
    conn, cur = connectDB()
    query_insert = "INSERT INTO pasien(email, user_password, nama, alamat, tanggal_lahir, no_telp, jenis_kelamin) VALUES(%s, %s, %s, %s, %s, %s, %s)"

    cur.execute(query_insert, (email, user_password, nama, alamat, tanggal_lahir, no_telp, jenis_kelamin))
    conn.commit()
    conn.close()

def addRekamMedis(idbooking, diagnosa, tindakan, catatan):
    conn, cur = connectDB()
    query_insert = "INSERT INTO rekam_medis(id_booking, diagnosa, tindakan, catatan_dokter) VALUES(%s, %s, %s, %s)"
    cur.execute(query_insert, (idbooking, diagnosa, tindakan, catatan))
    conn.commit()
    conn.close()

def addResepObat(idrm, ambil2, quantity, frekuensi):
    conn, cur = connectDB()
    query_insert = "INSERT INTO resep_obat(id_rekam_medis, id_obat, quantity, frekuensi) VALUES(%s, %s, %s, %s)"
    cur.execute(query_insert, (idrm, ambil2, quantity, frekuensi))
    conn.commit()
    conn.close()

def addTagihan(id_booking, tanggal_transaksi, metode_pembayaran, status_pembayaran):
    conn, cur = connectDB()
    query_insert = "INSERT INTO transaksi(id_booking, tanggal_transaksi, metode_pembayaran, status_pembayaran) VALUES(%s, %s, %s, %s)"
    cur.execute(query_insert, (id_booking, tanggal_transaksi, metode_pembayaran, status_pembayaran))
    conn.commit()
    conn.close()

def addObat(nama_obat, jenis_obat, stok_obat, harga_obat):
    conn, cur = connectDB()
    query_insert = "INSERT INTO obat(nama_obat, jenis_obat, stok_obat, harga_obat) VALUES(%s, %s, %s, %s)"
    cur.execute(query_insert, (nama_obat, jenis_obat, stok_obat, harga_obat))
    conn.commit()
    conn.close()

def addDokter(email, user_password, nama, spesialisasi, alamat, no_telp, biaya_konsultasi):
    conn, cur = connectDB()
    query_insert = "INSERT INTO obat(email, user_password, nama, spesialisasi, alamat, no_telp, biaya_konsultasi) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(query_insert, (email, user_password, nama, spesialisasi, alamat, no_telp, biaya_konsultasi))
    conn.commit()
    conn.close()

def addJadwal(id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking):
    conn, cur = connectDB()
    query_insert = "INSERT INTO obat(id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking) VALUES(%s, %s, %s, %s, %s)"
    cur.execute(query_insert, (id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking))
    conn.commit()
    conn.close()

#--------------------------------------------------------------------------------------------------

def updateDataObat(nama_obat, jenis_obat, stok_obat, harga_obat, id_obat):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE obat SET nama_obat = %s, jenis_obat = %s, stok_obat = %s, harga_obat = %s WHERE id_obat = %s"        
        cur.execute(query_update, (nama_obat, jenis_obat, stok_obat, harga_obat, id_obat))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None
    
def updateDataPasien(email, user_password, nama, alamat, tanggal_lahir, no_telp, jenis_kelamin, id_pasien):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE pasien SET email = %s, user_password = %s, nama = %s, alamat = %s, tanggal_lahir = %s, no_telp = %s, jenis_kelamin = %s WHERE id_pasien = %s"        
        cur.execute(query_update, (email, user_password, nama, alamat, tanggal_lahir, no_telp, jenis_kelamin, id_pasien))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None
    
def updateDataDokter(email, user_password, nama, spesialisasi, alamat, no_telp, biaya_konsultasi, id_dokter):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE dokter SET email = %s, user_password = %s, nama = %s, spesialisasi = %s, alamat = %s, no_telp = %s, biaya_konsultasi = %s WHERE id_dokter = %s"        
        cur.execute(query_update, (email, user_password, nama, spesialisasi, alamat, no_telp, biaya_konsultasi, id_dokter))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None
    
def updateDataJadwal(id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking, id_jadwal):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE jadwal SET id_dokter = %s, jadwal_praktik = %s, jam_mulai = %s, jam_selesai = %s, batas_booking = %s WHERE id_jadwal = %s"        
        cur.execute(query_update, (id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking, id_jadwal))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None
    
def updateStatusBooking(status_konsultasi, id_booking):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE booking_konsultasi SET status_konsultasi = %s WHERE id_booking = %s"        
        cur.execute(query_update, (status_konsultasi, id_booking))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None
    
def updateStatusTransaksi(status_pembayaran, id_transaksi):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE transaksi SET status_pembayaran = %s WHERE id_transaksi = %s"        
        cur.execute(query_update, (status_pembayaran, id_transaksi))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None
    
def updateMetodeTransaksi(status_konsultasi, id_transaksi):
    try:
        conn, cur = connectDB()
        query_update = "UPDATE transaksi SET metode_pembayaran = %s WHERE id_transaksi = %s"        
        cur.execute(query_update, (status_konsultasi, id_transaksi))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()
        return None

#--------------------------------------------------------------------------------------------------

def deleteObatById(id):
    try :
        conn, cur = connectDB()
        query_delete = "DELETE * FROM obat WHERE id_obat = %s"
        cur.execute(query_delete, (id,))
        conn.commit()
        conn.close()
    except Exception :
        conn.rollback()
        conn.close()
        return None
    
def deletePasienById(id):
    try :
        conn, cur = connectDB()
        query_delete = "DELETE * FROM pasien WHERE id_pasien = %s"
        cur.execute(query_delete, (id,))
        conn.commit()
        conn.close()
    except Exception :
        conn.rollback()
        conn.close()
        return None

def deleteDokterById(id):
    try :
        conn, cur = connectDB()
        query_delete = "DELETE * FROM dokter WHERE id_dokter = %s"
        cur.execute(query_delete, (id,))
        conn.commit()
        conn.close()
    except Exception :
        conn.rollback()
        conn.close()
        return None
    
def deleteJadwalById(id):
    try :
        conn, cur = connectDB()
        query_delete = "DELETE * FROM jadwal_konsultasi WHERE id_jadwal = %s"
        cur.execute(query_delete, (id,))
        conn.commit()
        conn.close()
    except Exception :
        conn.rollback()
        conn.close()
        return None

#--------------------------------------------------------------------------------------------------

def getAllObat():
    conn, cur = connectDB()
    query_select = "SELECT * FROM obat"

    cur.execute(query_select)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_obat", "nama_obat", "jenis_obat", "stok_obat", "harga_obat"])
    data.index += 1
    conn.close()
    return data

def getAllPasien():
    conn, cur = connectDB()
    query_select = "SELECT * FROM pasien"
    cur.execute(query_select)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_pasien", "email", "password", "nama", "alamat", "tanggal lahir", "no telp", "jenis kelamin"])
    data.index += 1
    conn.close()
    return data

def getAllDokter():
    conn, cur = connectDB()
    query_select = "SELECT * FROM dokter"

    cur.execute(query_select)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_dokter", "email", "password", "nama", "spesialisasi", "alamat", "no_telp", "biaya_konsultasi"])
    data.index += 1
    conn.close()
    return data

def getAllAdmin():
    conn, cur = connectDB()
    query_select = "SELECT * FROM admin"

    cur.execute(query_select)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_admin", "email", "password", "nama", "no_telp"])
    data.index += 1
    conn.close()
    return data

def getAllJadwal():
    conn, cur = connectDB()
    query_select = "SELECT * FROM jadwal_konsultasi"

    cur.execute(query_select)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_jadwal", "id_dokter", "jadwal_praktik", "jam_mulai", "jam_selesai", "batas_booking"])
    data.index += 1
    conn.close()
    return data

#-------------------------------------------------------------------------------------------

def menuadmin(nama):
    while (True):
        header("Dashboard Admin")
        print(f"Selamat Datang Kembali, {nama}!\n")
        input1 = int(input("[1]Kelola Obat\n[2]Kelola Pasien\n[3]Kelola Dokter\n[4]Kelola Jadwal\n[5]Kelola Reservasi\n[6]Tagihan dan Transaksi\n[0]Keluar\n\nPilih menu : "))
        dataobat = getAllObat()
        datapasien = getAllPasien()
        datadokter = getAllDokter()
        datajadwal = getAllJadwal()
        match input1:
            case 1:
                while True:
                    header("Kelola Obat")
                    input1 = int(input("[1]Lihat Data Obat\n[2]Tambahkan Data Obat\n[3]Ubah Data Obat\n[4]Hapus Data Obat\n[0]Keluar\nMasukkan pilihan (1/2/3/4/0) : "))
                    match input1:
                        case 1:
                            print(dataobat)
                            input("(Enter untuk melanjutkan.)")
                        case 2 :
                            nama_obat = input("Nama obat \t: ")
                            jenis_obat = input("Jenis Obat \t: ")
                            stok_obat = int(input("Stok obat (angka) \t: "))
                            harga_obat = int(input("Harga obat (angka) \t: "))
                            addObat(nama_obat, jenis_obat, stok_obat, harga_obat)
                            input(f"|    Data {nama_obat}berhasil ditambahkan! \n(Enter untuk kembali.)")
                        case 3 :
                            print(dataobat)
                            id_obat = input("Masukkan id obat \t:")
                            nama_obat = input("Masukkan data baru\nNama obat \t: ")
                            jenis_obat = input("Jenis Obat \t: ")
                            stok_obat = int(input("Stok obat (angka) \t: "))
                            harga_obat = int(input("Harga obat (angka) \t: "))
                            updateDataObat(nama_obat, jenis_obat, stok_obat, harga_obat, id_obat)
                            input("|    Data berhasil diperbarui!\n(Enter untuk kembali.)")
                        case 4 :
                            print(dataobat)
                            id_obat = input("Masukkan id obat \t:")
                            deleteObatById(id_obat)
                            input("|    Data berhasil dihapus!\n(Enter untuk kembali.)")
                        case 0:
                            break
                        case _:
                            input("|   Input tidak valid, dianggap 'Tidak'. \n(Enter untuk kembali.)")
                            break
            case 2:
                while True:
                    header("Kelola Pasien")
                    input2 = int(input("[1]Lihat Data Pasien\n[2]Ubah Data Pasien\n[3]Hapus Data Pasien\n[0]Keluar\nMasukkan pilihan (1/2/3/0) : "))
                    match input2:
                        case 1:
                            print(datapasien)
                            input("(Enter untuk kembali.)")
                        case 2 :
                            print(datapasien)
                            id_pasien = input("Masukkan id pasien \t:")
                            baris = datapasien[datapasien['id_pasien'] == id_pasien]
                            tanya = int(input("[1]Email dan Password\n[2]Data Diri Pasien\nMasukkan pilihan (1/2):"))
                            match tanya:
                                case 1:
                                    email = input("Masukkan email baru\t:")
                                    user_password = input("Masukkan password baru \t:")
                                    namapasien = baris['nama'].values[0]
                                    alamat = baris['alamat'].values[0]
                                    tanggal_lahir = baris['tanggal_lahir'].values[0]
                                    no_telp = baris['no_telp'].values[0]
                                    jenis_kelamin = baris['jenis_kelamin'].values[0]
                                case 2:
                                    email = baris['email'].values[0]
                                    user_password = baris['user_password'].values[0]
                                    namapasien = input("Nama \t\t:")
                                    alamat = input("Alamat \t\t:")
                                    tanggal_lahir = datetime.strptime(input("Tanggal Lahir (YYYY-MM-DD) \t:"), "%Y-%m-%d").date()
                                    no_telp = input ("Nomor Telepon \t:")
                                    jenis_kelamin = (input("Jenis Kelamin (L/P) \t:")).lower()
                                    if jenis_kelamin == 'p':
                                        jenis_kelamin = "Perempuan"
                                    else :
                                        jenis_kelamin = "Laki-laki"
                            updateDataPasien(email, user_password, namapasien, alamat, tanggal_lahir, no_telp, jenis_kelamin, id_pasien)
                            input("|    Data berhasil diperbarui!\n(Enter untuk kembali.)")
                        case 3 :
                            print(datapasien)
                            id_obat = input("Masukkan id pasien \t:")
                            deletePasienById(id_pasien)
                            input("|    Data berhasil dihapus!\n(Enter untuk kembali.)")
                        case 0:
                            break
                        case _:
                            input("|   Input tidak valid, dianggap 'Tidak'. \n(Enter untuk melanjutkan.)")
                            break
            case 3:
                while True:
                    header("Kelola Dokter")
                    input3 = int(input("[1]Lihat Data Dokter\n[2]Tambahkan Data Dokter\n[3]Ubah Data Dokter\n[4]Hapus Data Dokter\n[0]Keluar\nMasukkan pilihan (1/2/3/4/0) : "))
                    match input3:
                        case 1:
                            print(datadokter)
                            input("(Enter untuk melanjutkan.)")
                        case 2 :
                            email = input("Email \t:")
                            user_password = input("Password \t:")
                            nama_dokter = input("Nama Lengkap \t\t: ")
                            spesialisasi = input("Spesialisasi \t\t:")
                            alamat = input("Alamat \t\t:")
                            no_telp = input("No Telepon \t\t:")
                            biaya_konsultasi = input("Biaya Konsultasi \t:")
                            addDokter(email, user_password, nama_dokter, spesialisasi, alamat, no_telp, biaya_konsultasi)
                            input(f"|    Data {nama_dokter} berhasil ditambahkan! \n(Enter untuk kembali.)")
                        case 3 :
                            print(datadokter)
                            id_dokter = input("Masukkan id dokter \t:")
                            barisdokter = datadokter[datadokter['id_dokter'] == id_dokter]
                            tanya = int(input("[1]Email dan Password\n[2]Data Diri Dokter\nMasukkan pilihan (1/2):"))
                            match tanya:
                                case 1 :
                                    email = input("Email \t:")
                                    user_password = input("Password \t:")
                                    nama_dokter = barisdokter['nama'].values[0]
                                    spesialisasi = barisdokter['spesialisasi'].values[0]
                                    alamat = barisdokter['alamat'].values[0]
                                    no_telp = barisdokter['no_telp'].values[0]
                                    biaya_konsultasi = barisdokter['biaya_konsultasi'].values[0]
                                case 2 :
                                    email = barisdokter['email'].values[0]
                                    user_password = barisdokter['user_password'].values[0]
                                    nama_dokter = input("Nama Lengkap \t\t: ")
                                    spesialisasi = input("Spesialisasi \t\t:")
                                    alamat = input("Alamat \t\t:")
                                    no_telp = input("No Telepon \t\t:")
                                    biaya_konsultasi = input("Biaya Konsultasi \t:")
                            updateDataDokter(email, user_password, nama_dokter, spesialisasi, alamat, no_telp, biaya_konsultasi, id_dokter)
                            input("|    Data berhasil diperbarui!\n(Enter untuk melanjutkan.)")
                        case 4 :
                            print(datadokter)
                            id_dokter = input("Masukkan id dokter \t:")
                            deleteDokterById(id_dokter)
                            input("|    Data berhasil dihapus!\n(Enter untuk kembali.)")
                        case 0:
                            break
                        case _:
                            input("|   Input tidak valid, dianggap 'Tidak'. \n(Enter untuk melanjutkan.)")
                            break
            case 4:
                while True:
                    header("Kelola Jadwal")

                    conn, cur = connectDB()
                    query_select = "SELECT jk.id_jadwal, d.nama, jk.jadwal_praktik, jk.jam_mulai, jk.jam_selesai, jk.batas_booking FROM jadwal_konsultasi jk\
                        JOIN dokter d on jk.id_dokter = d.id_dokter"
                    cur.execute(query_select)
                    datajadwaltampil = cur.fetchall()
                    datajadwaltampil = pd.DataFrame(datajadwaltampil, columns=["id_jadwal", "id_dokter", "jadwal_praktik", "jam_mulai", "jam_selesai", "batas_booking"])
                    datajadwaltampil.index += 1
                    conn.close()

                    input1 = int(input("[1]Lihat Data Jadwal\n[2]Tambahkan Data Jadwal\n[3]Ubah Data Jadwal\n[4]Hapus Data Jadwal\n[0]Keluar\nMasukkan pilihan (1/2/3/4/0) : "))
                    match input1:
                        case 1:
                            print(datajadwaltampil)
                            input("(Enter untuk kembali.)")
                        case 2 :
                            print(datadokter)
                            id_dokter = int(input("Masukkan id dokter \t: "))
                            jadwal_praktik = int(input("[1]Sunday\n[2]Monday\n[3]Tuesday\n[4]Wednesday\n[5]Thursday\n[6]Friday\n[7]Saturday\n\nMasukkan hari (1/2/3/4/5/6/7) :"))
                            match jadwal_praktik:
                                case 1 :
                                    jadwal_praktik = 'Sunday'
                                case 2 :
                                    jadwal_praktik = 'Monday'
                                case 3 :
                                    jadwal_praktik = 'Tuesday'
                                case 4 :
                                    jadwal_praktik = 'Wednesday'
                                case 5 :
                                    jadwal_praktik = 'Thursday'
                                case 6 :
                                    jadwal_praktik = 'Friday'
                                case 7 :
                                    jadwal_praktik = 'Saturday'
                                case _ :
                                    jadwal_praktik = 'Sunday'
                            jam_mulai = input("Jam mulai (misal 08:00)\t\t:")
                            jam_mulai = datetime.strptime(jam_mulai, "%H:%M").time()
                            jam_selesai = input("Jam mulai (misal 08:00)\t\t:")
                            jam_selesai = datetime.strptime(jam_selesai, "%H:%M").time()
                            batas_booking = int(input("Batas booking (angka)\t:"))
                            addJadwal(id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking)
                            input(f"|    Data berhasil ditambahkan! \n(Enter untuk kembali.)")
                        case 3 :
                            print(datajadwaltampil)
                            id_jadwal = input("Masukkan id jadwal \t:")
                            barisjadwal = datajadwal[datajadwal['id_jadwal'] == id_jadwal]
                            id_dokter = barisjadwal['id_dokter'].values[0]
                            jadwal_praktik = int(input("[1]Sunday\n[2]Monday\n[3]Tuesday\n[4]Wednesday\n[5]Thursday\n[6]Friday\n[7]Saturday\n\nMasukkan hari (1/2/3/4/5/6/7) :"))
                            match jadwal_praktik:
                                case 1 :
                                    jadwal_praktik = 'Sunday'
                                case 2 :
                                    jadwal_praktik = 'Monday'
                                case 3 :
                                    jadwal_praktik = 'Tuesday'
                                case 4 :
                                    jadwal_praktik = 'Wednesday'
                                case 5 :
                                    jadwal_praktik = 'Thursday'
                                case 6 :
                                    jadwal_praktik = 'Friday'
                                case 7 :
                                    jadwal_praktik = 'Saturday'
                                case _ :
                                    jadwal_praktik = 'Sunday'
                            jam_mulai = input("Jam mulai (misal 08:00)\t\t:")
                            jam_mulai = datetime.strptime(jam_mulai, "%H:%M").time()
                            jam_selesai = input("Jam mulai (misal 08:00)\t\t:")
                            jam_selesai = datetime.strptime(jam_selesai, "%H:%M").time()
                            batas_booking = int(input("Batas booking (angka)\t:"))
                            addJadwal(id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking, id_jadwal)
                            input(f"|    Data berhasil diperbarui! \n(Enter untuk kembali.)")
                        case 4 :
                            print(datajadwaltampil)
                            id_jadwal = input("Masukkan id jadwal \t:")
                            deleteJadwalById(id_jadwal)
                            input("|    Data berhasil dihapus!\n(Enter untuk kembali.)")
                        case 0:
                            break
                        case _:
                            input("|   Input tidak valid, dianggap 'Tidak'. \n(Enter untuk melanjutkan.)")
                            break
            case 5:
                while True:
                    header("Kelola Reservasi")

                    conn, cur = connectDB()
                    query_select = "SELECT p.nama, d.nama, jk.id_jadwal, jk.jadwal_praktik, jk.jam_mulai, jk.jam_selesai, bk.tanggal_booking, bk.no_antrian, bk.status_konsultasi FROM pasien p\
                        JOIN booking_konsultasi bk on p.id_pasien = bk.id_pasien \
                        JOIN jadwal_konsultasi jk on bk.id_jadwal = jk.id_jadwal \
                        JOIN dokter d on jk.id_dokter = d.id_dokter"
                    cur.execute(query_select)
                    datareservasitampil = cur.fetchall()
                    datareservasitampil = pd.DataFrame(datareservasitampil, columns=["nama pasien", "nama dokter", "id jadwal", "jadwal praktik", "jam mulai", "jam selesai", "tanggal booking", "no antrian", "status"])
                    datareservasitampil.index += 1
                    conn.close()

                    input1 = int(input("[1]Lihat Data Booking\n[2]Ubah Status Booking\n[0]Keluar\nMasukkan pilihan (1/2/3/0) : "))
                    match input1:
                        case 1:
                            print(datareservasitampil)
                            input("(Enter untuk kembali.)")
                        case 2 :
                            print(datareservasitampil)
                            id_booking = input("Masukkan id booking \t:")
                            status_konsultasi = input("[1]menunggu\n[2]selesai\n[3]dibatalkan")
                            updateStatusBooking(status_konsultasi, id_booking)
                            input(f"|    Data berhasil diperbarui! \n(Enter untuk kembali.)")
                        case 0:
                            break
                        case _:
                            input("|   Input tidak valid, dianggap 'Tidak'. \n(Enter untuk melanjutkan.)")
                            break
            case 6:
                header("Tagihan dan Transaksi")
                conn, cur = connectDB()
                query_select = "SELECT t.id_transaksi, p.nama, bk.tanggal_booking + ((CASE jk.jadwal_praktik WHEN 'Sunday' THEN 0 WHEN 'Monday' THEN 1 WHEN 'Tuesday' THEN 2 WHEN 'Wednesday' THEN 3 WHEN 'Thursday' THEN 4 \
                WHEN 'Friday' THEN 5 WHEN 'Saturday' THEN 6 END - EXTRACT(DOW FROM bk.tanggal_booking)::int + 7) % 7) + 1 AS tanggal_pemeriksaan,\
                t.tanggal_transaksi, t.metode_pembayaran, t.status_pembayaran FROM pasien p \
                JOIN booking_konsultasi bk on p.id_pasien = bk.id_pasien \
                JOIN jadwal_konsultasi jk on bk.id_jadwal = jk.id_jadwal \
                JOIN transaksi t on bk.id_booking = t.id_booking"
                cur.execute(query_select)
                data = cur.fetchall()
                data = pd.DataFrame(data, columns=["id transaksi", "nama pasien", "tanggal pemeriksaan", "tanggal transaksi", "metode pembayaran", "status pembayaran"])
                data.index += 1
                conn.close()
                print(data)
                idtransaksi = int(input("Masukkan id transaksi \t:"))
                inputan = int(input("[1]Ubah Metode \n[2]Ubah Status"))
                match inputan:
                    case 1:
                        metode = int(input("[1]tunai\n[2]transfer\n[3]e-wallet\n[4]debit\n[5]kredit\nMasukkan pilihan (1/2/3/4/5) :"))
                        match metode:
                            case 2 :
                                metode = 'transfer'
                            case 3 :
                                metode = 'e-wallet'
                            case 5 :
                                metode = 'debit'
                            case 6 :
                                metode = 'kredit'
                            case _ :
                                metode = 'tunai'
                        updateMetodeTransaksi(metode, idtransaksi)
                    case 2:
                        status = int(input("[1]belum bayar\n[2]lunas\n[3]menunggu\nMasukkan pilihan (1/2/3) :"))
                        match status :
                            case 2:
                                status = 'belum bayar'
                            case 3:
                                status = 'lunas'
                            case _:
                                status = 'menunggu'
                    case _:
                        print("|    Inputan tidak valid, Anda akan dikembalikan. \n(Enter untuk melanjutkan.)")
            case 0:
                header("Log out")
                print("\n        Terimakasih telah menggunakan layanan kami!^-^")
                print("\n───────────────────────────────────────────────────────────────")
                break
            case _:
                print("Inputan tidak valid. Silahkan coba kembali dan masukkan inputan yang benar.")
                input("(Enter untuk melanjutkan.)")
                break

menuadmin('Lia')
#-------------------------------------------------------------------------------------------

def jadwaldokter(nama):
    header("Lihat Jadwal")
    datadokter = getAllDokter()
    baris = datadokter[datadokter['nama'] == nama]
    iddokter = int(baris['id_dokter'].values[0])

    while (True):
        conn, cur = connectDB()
        query = f"SELECT id_jadwal, jadwal_praktik, jam_mulai, jam_selesai FROM jadwal_konsultasi WHERE id_dokter = {iddokter}"
        cur.execute(query)
        data = cur.fetchall()
        data = pd.DataFrame(data, columns=["id_jadwal", "jadwal_praktik", "jam_mulai", "jam_selesai"])
        data.index += 1
        idjadwal = data['id_jadwal'].values
        data.drop(columns=["id_jadwal"], inplace=True)
        print()
        print(data)
        conn.close()

        tanya1 = input("\nApakah Anda ingin melihat daftar pasien? (y/n)").lower()
        if tanya1 == 'y':
            pilih1 = int(input("Masukkan pilihan (angka):"))
            ambil = idjadwal[pilih1-1]

            conn, cur = connectDB()
            query = f"SELECT p.id_pasien, p.nama, p.tanggal_lahir, p.jenis_kelamin FROM pasien p\
                JOIN booking_konsultasi bk on p.id_pasien = bk.id_pasien \
                JOIN jadwal_konsultasi jk on bk.id_jadwal =  jk.id_jadwal \
                WHERE jk.id_jadwal = {ambil}"
            cur.execute(query)
            data = cur.fetchall()
            data = pd.DataFrame(data, columns=["id_pasien", "nama pasien", "tanggal lahir ", "jenis kelamin"])
            data.index += 1
            idpasien = data['id_pasien'].values
            data.drop(columns=["id_pasien"], inplace=True)
            print()
            print(data)
            conn.close()

            tanya2 = input("\nApakah Anda ingin melihat rekam medis pasien? (y/n)").lower()
            if tanya2 == 'y':
                pilih2 = int(input("Masukkan pilihan (angka) :"))
                ambil2 = idpasien[pilih2-1]

                conn, cur = connectDB()
                query = f"SELECT rm.diagnosa, rm.tindakan, rm.catatan_dokter, o.nama_obat, ro.quantity, ro.frekuensi FROM rekam_medis rm\
                    JOIN booking_konsultasi bk on rm.id_booking = bk.id_booking \
                    JOIN pasien p on bk.id_pasien =  p.id_pasien \
                    JOIN resep_obat ro on rm.id_rekam_medis = ro.id_rekam_medis \
                    JOIN obat o on ro.id_obat = o.id_obat \
                    WHERE p.id_pasien = {ambil2}"
                cur.execute(query)
                data = cur.fetchall()
                data = pd.DataFrame(data, columns=["diagnosa", "tindakan", "catatan dokter", "nama obat", "jumlah", "frekuensi"])
                data.index += 1
                print()
                print(data)
                conn.close()
                input("(Enter untuk kembali.)")
            elif tanya2 == 'n':
                break
            else :
                print("Input tidak valid. Dianggap 'Tidak'.")
                break
        elif tanya1 == 'n' :
            break
        else :
            print("Input tidak valid. Dianggap 'Tidak'.")
            break

def buathasilpemeriksaan(nama):
    header("Buat Hasil Pemeriksaan")
    conn, cur = connectDB()
    query = f"SELECT jk.jadwal_praktik, jk.jam_mulai, jk.jam_selesai, p.nama, bk.id_booking, bk.tanggal_booking + ((CASE jk.jadwal_praktik WHEN 'Sunday' THEN 0 WHEN 'Monday' THEN 1 WHEN 'Tuesday' THEN 2 WHEN 'Wednesday' THEN 3 WHEN 'Thursday' THEN 4 \
        WHEN 'Friday' THEN 5 WHEN 'Saturday' THEN 6 END - EXTRACT(DOW FROM bk.tanggal_booking)::int + 7) % 7) + 1 AS tanggal_pemeriksaan, p.id_pasien FROM jadwal_konsultasi jk \
        JOIN dokter d on jk.id_dokter = d.id_dokter \
        JOIN booking_konsultasi bk on jk.id_jadwal = bk.id_jadwal \
        JOIN pasien p on bk.id_pasien = p.id_pasien\
        WHERE d.nama ilike '{nama}'"
    cur.execute(query)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["hari praktik", "jam mulai", "jam selesai", "nama pasien", "id_booking", "tgl_transaksi", "id_pasien"])
    data.index += 1
    idbooking = data['id_booking'].values
    idpasien = data['id_pasien'].values
    tgltrans = data['tgl_transaksi'].values
    data.drop(columns=["id_booking", "id_pasien", "tgl_transaksi"], inplace=True)
    print()
    print(data)
    conn.close()
    pilih1 = int(input("Masukkan pilihan (angka):"))
    ambil = int(idbooking[pilih1-1])
    tgltrans = tgltrans[pilih1-1]

    print("\n[Masukkan Data Pemeriksaan]")
    diagnosa = input("Diagnosa \t\t:")
    tindakan = input("Tindakan \t\t:")
    catatan = input("Catatan \t\t:")
    
    print("\n[Masukkan Resep Obat]")
    conn, cur = connectDB()
    query = f"SELECT id_obat, nama_obat, jenis_obat, stok_obat FROM obat"
    cur.execute(query)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_obat", "nama obat", "jenis obat", "stok"])
    data.index += 1
    idobat = data['id_obat'].values
    data.drop(columns=["id_obat"], inplace=True)
    print()
    print(data)
    conn.close()
    pilih2 = int(input("Masukkan pilihan (angka):"))
    ambil2 = int(idobat[pilih2-1])
    quantity = int(input("Jumlah (angka) \t:"))
    frekuensi = input("Frekuensi pemakaian \t:")

    addRekamMedis(ambil, diagnosa, tindakan, catatan)

    conn, cur = connectDB()
    query_select = f"SELECT id_rekam_medis FROM rekam_medis WHERE id_booking = {ambil}"
    cur.execute(query_select)
    idrm = cur.fetchone()[0]

    addResepObat(idrm, ambil2, quantity, frekuensi)

    try:
        conn, cur = connectDB()
        query_update = f"UPDATE booking_konsultasi SET status_konsultasi = 'selesai' WHERE id_pasien = {idpasien}"
        cur.execute(query_update, ('selesai', idpasien))
        conn.commit()
        conn.close()
    except Exception:
        conn.rollback()

    addTagihan(ambil, tgltrans, 'tunai', 'belum bayar')


def menudokter(nama):
    while (True):
        header("Dashboard Dokter")
        input1 = int(input("[1]Lihat Jadwal\n[2]Buat hasil Pemeriksaan\n[0]Keluar\n\nPilih menu : "))
        match input1:
            case 1:
                jadwaldokter(nama)
            case 2:
                buathasilpemeriksaan(nama)
            case 0:
                header("Log out")
                print("\n        Terimakasih telah menggunakan layanan kami!^-^")
                print("\n───────────────────────────────────────────────────────────────")
                break
            case _:
                print("Inputan tidak valid. Silahkan coba kembali dan masukkan inputan yang benar.")
                input("(Enter untuk melanjutkan.)")

#--------------------------------------------------------------------------------------------------

def tagihanpembayaran(nama):
    header("Tagihan dan Pembayaran")
    datapasien = getAllPasien()
    baris = datapasien[datapasien['nama'] == nama]
    idpasien = int(baris['id_pasien'].values[0])
    pilihan = int(input("[1] Tagihan Aktif \n[2] Riwayat Pembayaran\n\nMasukkan pilihan :"))
    match pilihan:
        case 1:
            status = "belum bayar"
        case 2:
            status = "lunas"
    conn, cur = connectDB()
    query = f"SELECT t.tanggal_transaksi, t.metode_pembayaran, d.biaya_konsultasi + o.harga_obat*ro.quantity as biaya, t.status_pembayaran \
    FROM transaksi t \
    JOIN booking_konsultasi bk on t.id_booking = bk.id_booking \
    JOIN jadwal_konsultasi jk on bk.id_jadwal = jk.id_jadwal \
    JOIN dokter d on jk.id_dokter = d.id_dokter \
    JOIN rekam_medis rm on bk.id_booking = rm.id_booking \
    JOIN resep_obat ro on rm.id_rekam_medis = ro.id_rekam_medis \
    JOIN obat o on ro.id_obat = o.id_obat \
    WHERE bk.id_pasien = {idpasien} and t.status_pembayaran = '{status}'"
    cur.execute(query)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["tanggal_transaksi", "metode_pembayaran", "biaya", "status_pembayaran"])
    data.index += 1
    conn.close()
    match pilihan:
        case 1:
            header("Tagihan Aktif")
            if data.empty:
                print("Belum ada tagihan aktif.")
            else : print(data)
        case 2:
            header("Riwayat Pembayaran")
            if data.empty:
                print("Belum ada riwayat pembayaran.")
            else : print(data)
    input("(Enter untuk melanjutkan.)")

def daftarpemeriksaan(nama):
    header("Daftar Pemeriksaan Online")
    pilih1 = int(input("Spesialisasi\n------------\n[1]Umum\n[2]Anak\n[3]Gigi\nMasukkan pilihan anda (1/2/3): "))
    keluhan = input("\nMasukkan keluhan Anda \t\t:")
    detail_keluhan = input("Masukkan detail keluhan Anda \t:")
    conn, cur = connectDB()
    match pilih1:
        case 1 :
            query = "SELECT id_dokter, nama, spesialisasi, biaya_konsultasi FROM dokter WHERE spesialisasi = 'Umum'"
        case 2 :
            query = "SELECT id_dokter, nama, spesialisasi, biaya_konsultasi FROM dokter WHERE spesialisasi = 'Anak'"
        case 3 : 
            query = "SELECT id_dokter, nama, spesialisasi, biaya_konsultasi FROM dokter WHERE spesialisasi = 'Gigi'"
    cur.execute(query)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["id_dokter", "nama", "spesialisasi", "biaya_konsultasi"])
    data.index += 1
    iddokter = data['id_dokter'].values
    data.drop(columns=["id_dokter"], inplace=True)
    print(data)
    conn.close()
    pilih2 = int(input("Masukkan pilihan (angka):"))
    ambil = iddokter[pilih2-1]

    conn, cur = connectDB()
    query = f"SELECT d.nama, jd.id_jadwal, jd.jadwal_praktik, jd.jam_mulai, jd.jam_selesai FROM dokter d JOIN jadwal_konsultasi jd on d.id_dokter = jd.id_dokter WHERE d.id_dokter = {ambil}"
    cur.execute(query)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["nama", "id_jadwal", "hari praktik", "jam mulai", "jam selesai"])
    data.index += 1
    idjadwal = data['id_jadwal'].values
    data.drop(columns=["id_jadwal"], inplace=True)
    print(data)
    conn.close()
    pilih3 = int(input("Masukkan pilihan anda (angka) :"))
    id_diambil = int(iddokter[pilih3-1])

    datapasien = getAllPasien()
    baris = datapasien[datapasien['nama'] == nama]
    idpasien = int(baris['id_pasien'].values[0])
    
    tglskrg = date.today()

    conn, cur = connectDB()
    query = f"SELECT * FROM booking_konsultasi WHERE status_konsultasi = 'menunggu' and id_jadwal = {id_diambil}"
    cur.execute(query)
    data = cur.fetchall()
    noantri=1
    for row in data:
        noantri+=1

    conn, cur = connectDB()
    query_insert = "INSERT INTO booking_konsultasi(id_pasien, id_jadwal, no_antrian, tanggal_booking) VALUES(%s, %s, %s, %s)"
    cur.execute(query_insert, (idpasien, id_diambil, noantri, tglskrg))
    conn.commit()
    conn.close()

def statusantrian(nama):
    header("Lihat status Antrian")
    datapasien = getAllPasien()
    baris = datapasien[datapasien['nama'] == nama]
    idpasien = int(baris['id_pasien'].values[0])
    conn, cur = connectDB()
    query = f"SELECT id_jadwal, no_antrian FROM booking_konsultasi WHERE id_pasien = {idpasien}"
    cur.execute(query)
    databookingku = cur.fetchall()
    databookingku = pd.DataFrame(databookingku, columns=["id_jadwal", "no_antrian"])
    conn.close()

    keterangan = []
    for i in range(len(databookingku)):
        idjadwalnow = int(databookingku['id_jadwal'].values[i])
        antriankunow = int(databookingku['no_antrian'].values[i])

        conn, cur = connectDB()
        query = f"SELECT no_antrian FROM booking_konsultasi WHERE status_konsultasi = 'menunggu' and id_jadwal = {idjadwalnow}"
        cur.execute(query)
        dataallbooking = cur.fetchall()
        dataallbooking = pd.DataFrame(dataallbooking, columns=["no_antrian"])
        conn.close()

        hitung=0
        for j in range(len(dataallbooking)):
            if dataallbooking['no_antrian'].values[j] < antriankunow:
                hitung+=1
        if hitung < 0:
            keterangan.append(f"Masih ada {hitung} antrian sebelum Anda. Mohon bersabar.")
        else :
            keterangan.append("Tidak ada antrian sebelum Anda. Silahkan masuk ke ruangan sesuai jadwal.")
                
    conn, cur = connectDB()
    query = f"SELECT d.nama, jk.jadwal_praktik, jk.jam_mulai, jk.jam_selesai, bk.no_antrian FROM dokter d JOIN jadwal_konsultasi jk on d.id_dokter = jk.id_dokter JOIN booking_konsultasi bk on jk.id_jadwal = bk.id_jadwal WHERE bk.status_konsultasi = 'menunggu' and bk.id_pasien = {idpasien}"
    cur.execute(query)
    dataantrianku = cur.fetchall()
    dataantrianku = pd.DataFrame(dataantrianku, columns=["nama dokter", "jadwal praktik","jam mulai", "jam selesai", "no antrian"])
    conn.close()
    dataantrianku["keterangan"] = keterangan
    print(dataantrianku)
    input("\n(Enter untuk kembali.)")

def hasilpemeriksaan(nama):
    header("Hasil Pemeriksaan")
    datapasien = getAllPasien()
    baris = datapasien[datapasien['nama'] == nama]
    idpasien = int(baris['id_pasien'].values[0])
    conn, cur = connectDB()
    query= f"SELECT jk.jadwal_praktik, bk.tanggal_booking + ((CASE jk.jadwal_praktik WHEN 'Sunday' THEN 0 WHEN 'Monday' THEN 1 WHEN 'Tuesday' THEN 2 WHEN 'Wednesday' THEN 3 WHEN 'Thursday' THEN 4 \
    WHEN 'Friday' THEN 5 WHEN 'Saturday' THEN 6 END - EXTRACT(DOW FROM bk.tanggal_booking)::int + 7) % 7) + 1 AS tanggal_pemeriksaan, \
    rm.diagnosa, rm.tindakan, rm.catatan_dokter, o.nama_obat, ro.quantity, ro.frekuensi \
    FROM jadwal_konsultasi jk \
    JOIN booking_konsultasi bk on jk.id_jadwal = bk.id_jadwal \
    JOIN rekam_medis rm on bk.id_booking = rm.id_booking \
    JOIN resep_obat ro on rm.id_rekam_medis = ro.id_rekam_medis \
    JOIN obat o on ro.id_obat = o.id_obat \
    WHERE bk.id_pasien = {idpasien}"
    cur.execute(query)
    data = cur.fetchall()
    data = pd.DataFrame(data, columns=["hari", "tanggal pemeriksaan", "diagnosa", "tindakan", "catatan_dokter", "nama obat", "jumlah", "frekuensi"])
    data.index += 1
    conn.close()
    print(data)
    input("(Enter untuk melanjutkan.)")

def menupasien(nama):
    while (True):
        header("Dashboard Pasien")
        print(f"Selamat datang, {nama}!\nKelola kesehatan Anda dengan mudah melalui dashboard pasien.")
        pilihan = int(input("\n[1]Profil Dokter\n[2]Daftar Pemeriksaan Online\n[3]Lihat Status Antrian\n[4]Hasil Pemeriksaan\n[5]Tagihan dan Pembayaran\n[0]Keluar\n\nPilih menu:"))
        match pilihan :
            case 1:
                conn, cur = connectDB()
                query= "SELECT d.nama, d.spesialisasi, jd.jadwal_praktik, jd.jam_mulai, jd.jam_selesai FROM dokter d JOIN jadwal_konsultasi jd on d.id_dokter = jd.id_dokter"
                cur.execute(query)
                data = cur.fetchall()
                data = pd.DataFrame(data, columns=["nama dokter", "spesialisasi", "hari praktik", "jam mulai", "jam selesai"])
                data.index += 1
                print(data)
                conn.close()
                input("\n(Enter untuk kembali.)")
            case 2:
                daftarpemeriksaan(nama)
            case 3:
                statusantrian(nama)
            case 4:
                hasilpemeriksaan(nama)
            case 5:
                tagihanpembayaran(nama)
            case 0:
                header("Log out")
                print("\n        Terimakasih telah menggunakan layanan kami!^-^")
                print("\n───────────────────────────────────────────────────────────────")
                break
            case _:
                print("Inputan tidak valid. Silahkan coba kembali dan masukkan inputan yang benar.")
                input("(Enter untuk melanjutkan.)")

#---------------------------------------------------------------------------------------------

def login():
    email = input("Masukkan email :")
    password = input("Masukkan password :")
    datapasien = getAllPasien()
    datadokter = getAllDokter()
    dataadmin = getAllAdmin()
    if email in datapasien['email'].values:
        baris = datapasien[datapasien['email'] == email]
        if baris['password'].values[0] == password:
            input(f"Anda masuk sebagai {baris['nama'].values[0]}.\n(Enter untuk melanjutkan.)")
            menupasien(baris['nama'].values[0])
        else:
            print("Password salah.")
    elif email in datadokter['email'].values:
        baris = datadokter[datadokter['email'] == email]
        if baris['password'].values[0] == password:
            menudokter(baris['nama'].values[0])
        else:
            print("Password salah.")
    elif email in dataadmin['email'].values:
        baris = dataadmin[dataadmin['email'] == email]
        if baris['password'].values[0] == password:
            print("Login berhasil.") #nanti ke menu admin, belum
        else:
            print("Password salah.")

def signup():
    datapasien = getAllPasien()
    datadokter = getAllDokter()
    dataadmin = getAllAdmin()
    email = input("Masukkan email :")
    if email in datapasien['email'].values or email in datadokter['email'].values or email in dataadmin['email'].values:
        print("Maaf, email sudah terdaftar. Silahkan pakai email lain.")
    else : 
        password = input("Buat password :")
        input("\n(Enter untuk melanjutkan.)")
        header("Sign Up > Daftar sebagai Pasien")
        nama = input("Nama Lengkap\t\t:").capitalize()
        alamat = input("Alamat \t\t:")
        tgllahir = datetime.strptime(input("Tanggal Lahir (YYYY-MM-DD) \t:"), "%Y-%m-%d").date()
        notelp = input ("Nomor Telepon \t:")
        jenis_kelamin = (input("Jenis Kelamin (L/P) \t:")).lower()
        if jenis_kelamin == 'p':
            jenis_kelamin = "Perempuan"
        else :
            jenis_kelamin = "Laki-laki"
        input("(Enter untuk melanjutkan.)")
        addPasien(email, password, nama, alamat, tgllahir, notelp, jenis_kelamin)
        input("|  Anda berhasil terdaftar! \n|  Anda akan diarahkan ke menu pasien.\n\n(Enter untuk melanjutkan.)")
        menupasien(nama)

def homepage():
    header("Laman Awal")
    pilih = int(input("\n[1]Log in\n[2]Sign up\nPilih menu :"))
    match pilih:
        case 1:
            login()
        case 2:
            signup()
        case _:
            print("Maaf, input tidak valid.")

homepage()