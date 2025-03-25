# Selamat datang di Vending Machine AiCe!

## Deskripsi
Program ini mensimulasikan mesin penjual otomatis (vending machine) menggunakan konsep Deterministic Finite Automaton (DFA). Mesin ini menerima uang dalam nominal tertentu dan memungkinkan pengguna untuk membeli minuman jika saldo mencukupi.

## Isi Source Code
Dalam source code ini, dapat ditemukan:
1. vending_machine.py sebagai kode utama program vending machine
2. vending_machine_withRefund.py sebagai kode program yang sudah dimodifikasi untuk bisa melakukan fitur pengembalian
3. vending_dfa.txt sebagai dokumen konfigurasi
4. README.md sebagai dokumen pendukung

## Daftar Harga Minuman
Vending Machine AiCe menyediakan berbagai minuman:
1. Minuman A: Rp3.000,00
2. Minuman B: Rp4.000,00
3. Minuman C: Rp6.000,00

## Fitur Vending Machine AiCe
1. Menerima transaksi dengan pecahan Rp1000, Rp2000, Rp5000, dan Rp10000
2. Memroses transaksi berdasarkan transisi state yang didefinisikan dalam file konfigurasi
3. Menampilkan saldo dan daftar minuman yang dapat dibeli (A, B, dan C)
4. Menampilkan lintasan DFA yang telah dilalui

## Interaksi dengan Mesin
Untuk menggunakan Vending Machine AiCe, pengguna dapat:
1. Memasukkan uang sesuai nominal yang diterima (1000, 2000, 5000, 10000) sampai mencukupi harga minuman yang ingin dibeli.
2. Mesin akan menunjukkan saldo saat ini untuk membantu merekam jumlah uang yang sudah dimasukkan.
3. Setelah uang cukup untuk membeli, mesin akan menunjukkan status ON pada minuman yang bisa dibeli.
4. Pilih minuman dengan memasukkan "A", "B", atau "C"
5. Mesin akan mengeluarkan lintasan state DFA yang dilalui serta status pembelian (ACCEPTED atau REJECTED).
6. Mesin tidak melayani uang yang kurang maupun uang yang berlebih dari harga minuman yang dipilih.
7. Program akan berhenti setelah pengguna memilih minuman yang akan dibeli dan mengeluarkan hasilnya.

## Vending Machine dengan Fitur Pengembalian
Dalam folder ini, file vending_machine_withRefund.py adalah program yang sudah dimodifikasi untuk bisa melakukan fitur pengembalian. 

Untuk menggunakan Vending Machine AiCe dengan fitur pengembalian, pengguna dapat:
1. Memasukkan uang sesuai nominal yang diterima (1000, 2000, 5000, 10000) sampai mencukupi harga minuman yang ingin dibeli.
2. Mesin akan menunjukkan saldo saat ini untuk membantu merekam jumlah uang yang sudah dimasukkan.
3. Setelah uang cukup untuk membeli, mesin akan menunjukkan status ON pada minuman yang bisa dibeli.
4. Pilih minuman dengan memasukkan "A", "B", atau "C"
5. Mesin akan mengeluarkan lintasan state DFA yang dilalui serta status pembelian (ACCEPTED atau REJECTED).
6. Jika uang yang dimasukkan kurang dari harga minuman, mesin akan mengeluarkan status: REJECTED. Jika uang yang dimasukkan lebih dari harga minuman, mesin akan mengeluarkan status: ACCEPTED dan mengembalikan kembalian sisa saldo pengguna.
7. Setelah mengembalikan sisa saldo pengguna atau berhasil melakukan pembelian dengan saldo pas, mesin akan direset dan pengguna dapat melakukan proses lainnya (kembali ke step 1).
8. Pengguna dapat memasukkan 0 untuk berhenti.
