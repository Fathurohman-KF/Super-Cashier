# Latar Belakang
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibell, jumlah item yang dibell, dan harga item yang dibell dan fitur yang lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutukan Programmer untuk membuatkan fitur - fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar

# Requirements atau Objective

1. Costumer membuat ID transaksi customer dengan membuat object dari class. Sebagai contoh, trnsct_123 = Transaction()
2. Customer meng-input nama item, jumlah item, dan harga barang dengan method add_item()
3. Jika ternyata ada kesalahan dalam meng-input nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, customer bisa melakukan:

- Update nama item dengan method update_item_name()
- Update jumlah item dengan method update_item_qty()
- Update harga item dengan method update_item_price()

4. Jika batal membeli item belanjaan, Customer bisa melakukan:

- Menghapus salah satu item dari nama item dengan method delete_item()
- Langsung menghapus semua transaksi atau reset transaksi dengan method reset_transaction()

5. Customer bisa melakukan pengecekan pada status pemesanan sebelum membayar dengan method check_order() yang akan mengeluarkan output yaitu:

- Akan mengeluarkan pesan "Order is correct" jika tidak ada kesalahan input.
- Akan mengeluarkan pesan "There is a data input error" jika terjadi kesalahan input.

6. Keluaran output transaksi atau pemesanan apa saja yang sudah dibeli.
   Setelah melakukan checkout, Customer bisa menghitung total belanja dengan method total_price. Pada supermarket terdapat ketentuan:

- Jika total belanja diatas Rp 200.000 maka akan mendapatkan diskon 5%
- Jika total belanja diatas Rp 300.000 maka akan mendapatkan diskon 8%
- Jika total belanja diatas Rp 500.000 maka akan mendapatkan diskon 10%

# Flowchart

# Penjelasan

1. data_item = { "Nama item" : [], "Jumlah item" : [], "Harga item" : [], "Total harga" : []}
   = Untuk menampung data dalam transaksi
2. add_item (name, qty, price) = Untuk mnambahkan item di list transaksi
3. update_item_name (name, update_name) = untuk mengupdate nama item di dalam transaksi
4. update_item_qty (qty, update_qty) = Untuk mengupdate jumlah item pada transaksi
5. update_item_price (price, update_price) = Untuk melakukan perubahan harga pada transaksi
6. delete_item (delete_update) = Untuk menghapus atau membatalkan pada transaksi
7. reset_transaction() = Untuk membatalkan semua transaksi
8. check_order() = Untuk melakukan pengecekan pada seluruh item transaksi
9. total_price() = Untuk menghitung total harga belanja pada seluruh item transaksi

# Test Case
## Test 1:
### Customer ingin menambahkan dua item baru menggunakan method add_item () . Item yang ditambahkan adalah sebagai berikut:
• Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
• Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

## Test 2
### Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahki maka Customer menggunakan method delete_item () untuk menghapus item. Item y ingin dihapuskan adalah Pasta Gigi.

## Test 3
### Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan!
### Daripada menghapusnya satu - satu, maka Customer cukup menggunakan method reset_transaction () untuk menghapus semua item yang sudah ditambahkan.

## Test 4
### Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibay menggunakan method total_price () . Sebelum mengeluarkan output total belanja menampilkan item - item yang dibeli.

# Kesimpulan
Andi membuat program supermarket yang bertujuan untuk memudahkan customer dalam melakukan transaski di dalam supermarket.
Supermarket telah menjadi tempat yang sangat membantu bagi kebanyakan orang untuk memperoleh barang atau makanan yang mereka butuhkan. Supermarket menyediakan berbagai barang dalam satu tempat, memungkinkan orang untuk berbelanja secara efisien. Program ini akan meningkatkan efisiensi baik bagi customer maupun supermarket.

# Saran Pengembangan
*Bisa menambahkan database agar memperlancar program
*Pengembangan dalam metode pembayaran
