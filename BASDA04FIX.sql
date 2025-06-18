CREATE TYPE gender AS ENUM ('Laki-laki', 'Perempuan');

CREATE TABLE pasien (
id_pasien SERIAL PRIMARY KEY,
email VARCHAR (50) NOT NULL,
user_password VARCHAR (20) NOT NULL,
nama VARCHAR (100) NOT NULL,
alamat TEXT NOT NULL,
tanggal_lahir DATE NOT NULL,
no_telp VARCHAR (15) NOT NULL,
jenis_kelamin gender NOT NULL,
CONSTRAINT unique_pasien_email_no_telp UNIQUE(email, no_telp)
);

CREATE TABLE dokter (
id_dokter SERIAL PRIMARY KEY,
email VARCHAR (50) NOT NULL,
user_password VARCHAR (20) NOT NULL,
nama VARCHAR (100) NOT NULL,
spesialisasi VARCHAR (50) NOT NULL,
alamat TEXT NOT NULL,
no_telp VARCHAR (15) NOT NULL,
biaya_konsultasi INTEGER NOT NULL,
CONSTRAINT unique_dokter_email_no_telp UNIQUE(email, no_telp)
);

CREATE TABLE admin(
id_admin SERIAL PRIMARY KEY,
email VARCHAR (50) NOT NULL,
user_password VARCHAR (20) NOT NULL,
nama VARCHAR (100) NOT NULL,
no_telp VARCHAR (15) NOT NULL,
CONSTRAINT unique_admin_email_no_telp UNIQUE(email, no_telp)
);

CREATE TABLE obat (
id_obat SERIAL PRIMARY KEY,
nama_obat VARCHAR (100) NOT NULL,
jenis_obat VARCHAR (50),
stok_obat INTEGER NOT NULL,
harga_obat INTEGER NOT NULL
);

CREATE TYPE hari AS ENUM ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');

CREATE TABLE jadwal_konsultasi (
id_jadwal SERIAL PRIMARY KEY,
id_dokter INTEGER NOT NULL REFERENCES dokter(id_dokter),
jadwal_praktik hari NOT NULL,
jam_mulai TIME NOT NULL,
jam_selesai TIME NOT NULL,
batas_booking SMALLINT NOT NULL
);

CREATE TYPE statuskonsultasi AS ENUM ('menunggu', 'selesai', 'dibatalkan');

CREATE TABLE booking_konsultasi (
id_booking SERIAL PRIMARY KEY,
id_pasien INTEGER NOT NULL REFERENCES pasien(id_pasien),
id_jadwal INTEGER NOT NULL,
tanggal_booking DATE NOT NULL,
no_antrian INTEGER NOT NULL,
status_konsultasi statuskonsultasi DEFAULT 'menunggu' NOT NULL
);

CREATE TABLE rekam_medis (
id_rekam_medis SERIAL PRIMARY KEY,
id_booking INTEGER NOT NULL REFERENCES booking_konsultasi(id_booking),
diagnosa TEXT NOT NULL,
tindakan TEXT NOT NULL,
catatan_dokter TEXT
);

CREATE TABLE resep_obat (
id_rekam_medis INTEGER NOT NULL REFERENCES rekam_medis(id_rekam_medis),
id_obat INTEGER NOT NULL REFERENCES obat(id_obat),
quantity smallint NOT NULL,
frekuensi VARCHAR (50) NOT NULL
);

CREATE TYPE metodepembayaran AS ENUM ('tunai', 'transfer', 'e-wallet', 'debit', 'kredit');

CREATE TYPE statuspembayaran AS ENUM ('belum bayar', 'lunas', 'menunggu');

CREATE TABLE transaksi (
id_transaksi SERIAL PRIMARY KEY,
id_booking INTEGER NOT NULL REFERENCES booking_konsultasi(id_booking),
tanggal_transaksi DATE NOT NULL,
metode_pembayaran metodepembayaran NOT NULL,
status_pembayaran statuspembayaran DEFAULT 'belum bayar' NOT NULL
);

INSERT INTO pasien (email, user_password, nama, alamat, tanggal_lahir, no_telp, jenis_kelamin) VALUES
('rafiardianto@gmail.com', 'rafi123', 'Rafi Ardianto', 'Jl. Melati No. 12', '1995-03-15', '081234567001', 'Laki-laki'),
('bellaanggraini@gmail.com', 'bella123', 'Bella Anggraini', 'Jl. Kenanga No. 5', '1992-07-20', '081234567002', 'Perempuan'),
('budisantoso@gmail.com', 'budi123', 'Budi Santoso', 'Jl. Mawar No. 9', '1988-11-10', '081234567003', 'Laki-laki'),
('dinawulandari@gmail.com', 'dina123', 'Dina Wulandari', 'Jl. Flamboyan No. 21', '1997-02-25', '081234567004', 'Perempuan'),
('toniwijaya@gmail.com', 'toni123', 'Toni Wijaya', 'Jl. Dahlia No. 8', '1985-09-30', '081234567005', 'Laki-laki'),
('sarikusuma@gmail.com', 'sari123', 'Sari Kusuma', 'Jl. Anggrek No. 14', '1994-05-18', '081234567006', 'Perempuan'),
('rudihartono@gmail.com', 'rudi123', 'Rudi Hartono', 'Jl. Kenari No. 3', '1990-12-02', '081234567007', 'Laki-laki'),
('liaputri@gmail.com', 'lia123', 'Lia Putri', 'Jl. Melur No. 17', '1993-06-14', '081234567008', 'Perempuan'),
('yunimaulina@gmail.com', 'yuni123', 'Yuni Maulina', 'Jl. Cempaka No. 19', '1991-10-22', '081234567009', 'Perempuan'),
('andisubroto@gmail.com', 'andi123', 'Andi Subroto', 'Jl. Teratai No. 7', '1987-08-05', '081234567010', 'Laki-laki'),
('watirahman@gmail.com', 'wati123', 'Wati Rahman', 'Jl. Kamboja No. 13', '1996-04-08', '081234567011', 'Perempuan'),
('rezapratama@gmail.com', 'reza123', 'Reza Pratama', 'Jl. Melati No. 22', '1989-01-27', '081234567012', 'Laki-laki'),
('ninaamalia@gmail.com', 'nina123', 'Nina Amalia', 'Jl. Wijaya No. 6', '1992-12-11', '081234567013', 'Perempuan'),
('arifhidayat@gmail.com', 'arif123', 'Arif Hidayat', 'Jl. Rawa No. 15', '1990-07-03', '081234567014', 'Laki-laki'),
('lisaputri@gmail.com', 'lisa123', 'Lisa Putri', 'Jl. Bahagia No. 4', '1995-09-19', '081234567015', 'Perempuan'),
('tonokusuma@gmail.com', 'tono123', 'Tono Kusuma', 'Jl. Sari No. 11', '1988-03-21', '081234567016', 'Laki-laki'),
('raniwijaya@gmail.com', 'rani123', 'Rani Wijaya', 'Jl. Pelangi No. 18', '1991-06-30', '081234567017', 'Perempuan'),
('indrasantoso@gmail.com', 'indra123', 'Indra Santoso', 'Jl. Harapan No. 2', '1985-11-05', '081234567018', 'Laki-laki'),
('dewianggraini@gmail.com', 'dewi123', 'Dewi Anggraini', 'Jl. Mawar No. 16', '1993-08-28', '081234567019', 'Perempuan'),
('rioramadhan@gmail.com', 'rio123', 'Rio Ramadhan', 'Jl. Cendana No. 10', '1994-02-17', '081234567020', 'Laki-laki'),
('ninarohmah@gmail.com', 'nina123', 'Nina Rohmah', 'Jl. Sakura No. 1', '1989-10-07', '081234567021', 'Perempuan'),
('adipurwanto@gmail.com', 'adi123', 'Adi Purwanto', 'Jl. Melati No. 23', '1990-05-15', '081234567022', 'Laki-laki'),
('sintamulia@gmail.com', 'sinta123', 'Sinta Mulia', 'Jl. Kenanga No. 9', '1992-01-30', '081234567023', 'Perempuan'),
('yunipuspita@gmail.com', 'yuni123', 'Yuni Puspita', 'Jl. Anggrek No. 20', '1988-09-08', '081234567024', 'Perempuan'),
('ekoprasetyo@gmail.com', 'eko123', 'Eko Prasetyo', 'Jl. Mawar No. 7', '1996-03-26', '081234567025', 'Laki-laki');

INSERT INTO dokter (email, user_password, nama, spesialisasi, alamat, no_telp, biaya_konsultasi) VALUES
('budihartono@gmail.com', 'budi123', 'Budi Hartono', 'Umum', 'Jl. Kenanga No. 10', '081211112001', 50000),
('sriwahyuni@gmail.com', 'sri123', 'Sri Wahyuni', 'Anak', 'Jl. Melati No. 12', '081211112002', 45000),
('tonosubroto@gmail.com', 'tono123', 'Tono Subroto', 'Gigi', 'Jl. Mawar No. 5', '081211112003', 55000),
('watikusuma@gmail.com', 'wati123', 'Wati Kusuma', 'Umum', 'Jl. Anggrek No. 8', '081211112004', 45000),
('jonirahman@gmail.com', 'joni123', 'Joni Rahman', 'Umum', 'Jl. Cempaka No. 3', '081211112005', 50000);

INSERT INTO admin (email, user_password, nama, no_telp) VALUES
('parhan@gmail.com', 'parhan123', 'Farhan Syahbana', '081211113001'),
('lia@gmail.com', 'lia123', 'Kamelia Rizkiana', '081211114002'),
('desnii@gmail.com', 'desni123', 'Desni Eria', '081211115003');

INSERT INTO obat (nama_obat, jenis_obat, stok_obat, harga_obat) VALUES
('Paracetamol 500mg', 'Analgesik', 100, 2500),
('Amoxicillin 500mg', 'Antibiotik', 75, 3200),
('Cetirizine 10mg', 'Antihistamin', 50, 1800),
('Ibuprofen 400mg', 'Anti Inflamasi', 60, 3000),
('Metformin 500mg', 'Antidiabetes', 40, 3500),
('Salbutamol Inhaler', 'Bronkodilator', 30, 15000),
('Loperamide 2mg', 'Antidiare', 70, 2200),
('Ranitidine 150mg', 'Antasida', 55, 2800),
('Asam Mefenamat 500mg', 'Analgesik', 90, 2600),
('Amlodipine 5mg', 'Antihipertensi', 80, 3100),
('Omeprazole 20mg', 'Antasida', 65, 3300),
('Chlorpheniramine 4mg', 'Antihistamin', 45, 1700),
('Simvastatin 10mg', 'Antikolesterol', 50, 3400),
('Miconazole Cream', 'Antijamur', 25, 12000),
('Dexamethasone 0.5mg', 'Kortikosteroid', 70, 2400),
('Cotrimoxazole', 'Antibiotik', 60, 2900),
('Vitamin C 500mg', 'Vitamin', 100, 2000),
('Albendazole 400mg', 'Antelmintik', 35, 3600),
('Diazepam 2mg', 'Psikotropika', 20, 4500),
('Hydrocortisone Cream', 'Kortikosteroid', 15, 12500),
('Prednisone 5mg', 'Kortikosteroid', 40, 2600),
('Domperidone 10mg', 'Antiemetik', 45, 2700),
('Ketoconazole Shampoo', 'Antijamur', 20, 13500),
('Lorazepam 1mg', 'Psikotropika', 10, 4800),
('Furosemide 40mg', 'Diuretik', 55, 3000);

INSERT INTO jadwal_konsultasi (id_dokter, jadwal_praktik, jam_mulai, jam_selesai, batas_booking) VALUES
(1, 'Monday', '08:00:00', '12:00:00', 4),
(1, 'Wednesday', '08:00:00', '11:00:00', 3),
(1, 'Friday', '09:00:00', '12:00:00', 3),
(2, 'Tuesday', '10:00:00', '13:30:00', 4),
(2, 'Thursday', '09:00:00', '12:00:00', 3),
(2, 'Saturday', '08:00:00', '11:00:00', 3),
(3, 'Monday', '13:00:00', '16:00:00', 3),
(3, 'Thursday', '08:00:00', '11:30:00', 4),
(3, 'Friday', '14:00:00', '17:00:00', 3),
(4, 'Wednesday', '07:30:00', '10:30:00', 3),
(4, 'Friday', '10:00:00', '13:00:00', 3),
(4, 'Sunday', '09:00:00', '12:30:00', 4),
(5, 'Tuesday', '08:30:00', '11:30:00', 3),
(5, 'Thursday', '13:00:00', '16:00:00', 3),
(5, 'Saturday', '09:00:00', '12:00:00', 3);

INSERT INTO booking_konsultasi (id_pasien, id_jadwal, tanggal_booking, no_antrian, status_konsultasi) VALUES
(7,  3,  '2025-06-07', 1, 'menunggu'),
(14, 1,  '2025-06-07', 1, 'selesai'),
(11, 4,  '2025-06-07', 1, 'selesai'),
(3,  4,  '2025-06-07', 2, 'selesai'),
(22, 1,  '2025-06-07', 2, 'selesai'),
(25, 5,  '2025-06-07', 1, 'selesai'),
(5,  7,  '2025-06-08', 1, 'menunggu'),
(18, 10, '2025-06-09', 1, 'dibatalkan'),
(9,  12, '2025-06-10', 1, 'menunggu'),
(20, 15, '2025-06-11', 1, 'menunggu');

INSERT INTO rekam_medis (id_booking, diagnosa, tindakan, catatan_dokter) VALUES
(2, 'Demam dan batuk ringan', 'Pemberian parasetamol dan istirahat', 'Pasien disarankan banyak minum air putih'),
(3, 'Sakit kepala tegang', 'Pemberian ibuprofen', 'Perlu mengurangi waktu layar dan tidur cukup'),
(4, 'Diare akut', 'Oralit dan diet BRAT', 'Hindari makanan pedas dan berminyak'),
(5, 'Nyeri punggung bawah', 'Terapi panas dan analgesik', 'Perlu evaluasi postur duduk harian'),
(6, 'Radang tenggorokan', 'Antibiotik dan lozenges', 'Cek ulang dalam 3 hari');

INSERT INTO resep_obat (id_rekam_medis, id_obat, quantity, frekuensi) VALUES
(1, 1, 6, '3x sehari'),
(2, 4, 4, '2x sehari'),
(3, 7, 2, 'Setiap BAB cair'),
(4, 9, 5, '3x sehari'),
(5, 2, 5, '3x sehari');

INSERT INTO transaksi (id_booking, tanggal_transaksi, metode_pembayaran, status_pembayaran) VALUES
(2, '2025-06-07', 'tunai', 'lunas'),
(3, '2025-06-07', 'tunai', 'belum bayar'),
(4, '2025-06-07', 'transfer', 'lunas'),
(5, '2025-06-07', 'tunai', 'lunas'),
(6, '2025-06-07', 'kredit', 'menunggu');