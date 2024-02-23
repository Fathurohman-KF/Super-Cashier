from tabulate import tabulate

class Transaction:
    data_item = { 
        "Nama item"   : [], 
        "Jumlah item" : [], 
        "Harga item"  : [], 
        "Total harga" : []}

    def add_item(self, name, qty, price):
        '''
        Menambahkan item ke dalam transaksi.
        '''
        try:
            # Cek tipe data
            if type(name) != str:
                raise TypeError("Nama item harus berupa string.")
            if type(qty) != int:
                raise TypeError("Jumlah item harus berupa integer.")
            if type(price) != int:
                raise TypeError("Harga item harus berupa integer.")

            # Menambahkan item ke transaksi
            self.data_item["Nama item"].append(name)
            self.data_item["Jumlah item"].append(qty)
            self.data_item["Harga item"].append(price)
            total = qty * price
            self.data_item["Total harga"].append(total)

            return print(f'Harga item yang dibeli {self.data_item}')
        except TypeError:
            print(f"Terjadi kesalahan: Tipe data salah")

    def update_item_name(self, name, update_name ):
        '''
        Mengupdate nama item dalam transaksi.
        '''
        try:
            if type(name) != str:
                raise TypeError("Nama item harus berupa string.")
            if type(update_name) != str:
                raise TypeError("Nama item harus berupa string.")
            
            name_update = self.data_item["Nama item"].index(name)
            self.data_item["Nama item"][name_update] = update_name
            return print(f'Data nama item diubah{self.data_item}')
        
        except TypeError:
            print(f'Terjadi Kesalahan: Tipe data harus string')
        except ValueError:
            print(f'Nama item {update_name} tidak ditemukan dalam data.')


    def update_item_qty(self, qty, update_qty):
        '''
        Mengupdate jumlah item dalam transaksi.
        '''
        try:
            if type(qty) != str:
                raise TypeError("Nama item harus berupa string.")
            if type(update_qty) != str:
                raise TypeError("Nama item harus berupa string.")

            qty_update = self.data_item["Jumlah item"].index(qty)
            self.data_item["Jumlah item"][qty_update] = update_qty
            self.data_item["Total harga"][qty_update] = update_qty * \
            self.data_item["Harga item"][qty_update]
            return print(f'Data item yang diubah{self.data_item}')
           
        except TypeError:
           print(f'Terjadi kesalahan: Tipe data harus Integer')
        except ValueError:
            print(f'Nama item {update_qty} tidak ditemukan dalam data.')
    
    def update_item_price(self, price, update_price):

        '''
        Mengupdate harga item dalam transaksi.
        '''
        try:
            if type(price) != str:
                raise TypeError("Nama item harus berupa string.")
            if type(update_price) != str:
                raise TypeError("Nama item harus berupa string.")

            # Update harga dari suatu item
            price_update = self.data_item["Harga item"].index(price)
            self.data_item["Harga item"][price_update] = update_price
            self.data_item["Total harga"][price_update] = update_price * self.data_item["Jumlah item"][price_update]
            return print(f'Harga yang diupdate dari item {self.data_item}')
        
        except TypeError:
            print(f'Terjadi kesalahan: Tipe data harus Integer')
        except ValueError:
            print(f'Nama item {update_price} tidak ditemukan dalam data.')

    def delete_item(self, delete_update):
        '''
        Menghapus item dari transaksi.
        '''
        try:
            if type(delete_update) != str:
                raise TypeError("Nama item yang akan dihapus harus berupa string.")
            
            delete_index = self.data_item['Nama item'].index(delete_update)
            for key in self.data_item:
                self.data_item[key].pop(delete_index)
            return print(f'Data item yang dihapus{self.data_item}')
            
        except TypeError:
            print(f'Terjadi Kesalahan: Tipe data harus string')
        except ValueError:
            print(f'Nama item {delete_update} tidak ditemukan dalam data.')

    def reset_transaction(self):
        '''
        Menghapus semua item
        '''
        for key in self.data_item:
            self.data_item[key].clear()
        return print(f'Semua item dihapus')
    
    def check_order(self):
        '''
        Melakukan pengecekan terhadap seluruh item apakah terdapat nilai null.
        Jika semua item memiliki nilai, mencetak "Order tersedia".
        Jika ada item yang tidak memiliki nilai, mencetak "Order tidak ada".

        '''
        try:

        # Membuat dan mencetak tabel
            tabel = list(zip(*self.data_item.values()))
            headers = list(self.data_item.keys())
            tabel_str = tabulate(tabel, headers, tablefmt='github')
            print(tabel_str)

            check = True
            for item in self.data_item['Total harga']:
                if item <= 0:
                    check = False
            if check:
                print("Order tersedia")
            else:
                print("Order tidak ada")
        except TypeError:
            print(f"Terjadi kesalahan: Pastikan semua item memiliki harga.")

    def total_price(self):
        '''
        Menghitung total belanja dari transaksi, jika pembelian
        - lebih dari 200_000 maka mendapat diskon 5%
        - lebih dari 300_000 maka mendapat diskon 8%
        - lebih dari 500_000 maka mendapat diskon 10%
        '''
        try:
            total = sum(self.data_item['Total harga'])

            if total < 200000:
                pass
            elif total < 300000:
                total = total * 0.95
            elif total < 500000:
                total = total * 0.92
            else:
                total = total * 0.9

            return print(f'Total price : {total}')
        except TypeError :
            print(f"Terjadi kesalahan: Pastikan semua item memiliki harga.")