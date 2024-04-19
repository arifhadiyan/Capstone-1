from tabulate import tabulate

# Initialize grocery data
grocery_names = ['gula', 'minyak', 'beras']
grocery_stocks = [20, 15, 25]
grocery_prices = [10000, 15000, 20000]

shopping_cart = {}

# Function to display menu
def display_menu():
    print('Selamat datang di toko sembako.')
    print('Menu:')
    print('1. Menampilkan daftar barang')
    print('2. Menambah barang')
    print('3. Menghapus barang')
    print('4. Membeli barang')
    print('5. Keluar program')

# Function to display grocery list
def display_grocery_list():
    print('Daftar Barang Sembako:')
    headers = ['Barang', 'Stok', 'Harga']
    rows = []
    for i in range(len(grocery_names)):
        rows.append([grocery_names[i], grocery_stocks[i], grocery_prices[i]])
    print(tabulate(rows, headers=headers, tablefmt='grid'))

# Function to add grocery
def add_grocery():
    grocery_name = input('Masukkan nama barang baru: ').lower()
    if grocery_name in grocery_names:
        print('Barang sudah ada dalam daftar.')
    else:
        stock = int(input('Masukkan stok barang: '))
        price = int(input('Masukkan harga barang: '))
        grocery_names.append(grocery_name)
        grocery_stocks.append(stock)
        grocery_prices.append(price)
        print('Barang berhasil ditambahkan.')

# Function to remove grocery
def remove_grocery():
    grocery_name = input('Masukkan nama barang yang ingin dihapus: ').lower()
    if grocery_name in grocery_names:
        index = grocery_names.index(grocery_name)
        del grocery_names[index]
        del grocery_stocks[index]
        del grocery_prices[index]
        print('Barang berhasil dihapus.')
    else:
        print('Barang tidak ditemukan dalam daftar.')

# Function to buy grocery
def buy_grocery():
    total_payment = 0
    while True:
        display_grocery_list()
        grocery_name = input('Masukkan nama barang yang ingin dibeli: ').lower()
        if grocery_name in grocery_names:
            quantity = int(input('Masukkan jumlah barang yang ingin dibeli: '))
            if quantity > grocery_stocks[grocery_names.index(grocery_name)]:
                print('Stok tidak mencukupi.')
            else:
                if grocery_name in shopping_cart:
                    shopping_cart[grocery_name] += quantity
                else:
                    shopping_cart[grocery_name] = quantity
                grocery_stocks[grocery_names.index(grocery_name)] -= quantity
                total_payment += quantity * grocery_prices[grocery_names.index(grocery_name)]
                print('Barang berhasil ditambahkan ke keranjang belanja.')
        else:
            print('Barang tidak ditemukan dalam daftar.')

        buy_more = input('Apakah Anda ingin membeli barang lain? (ya/tidak): ').lower()
        if buy_more != 'ya':
            break

    print('Total Pembayaran:', total_payment)

    # Displaying total number of items in shopping cart
    total_items = sum(shopping_cart.values())
    print('Total Barang dalam Keranjang Belanja:', total_items)

    # Displaying detailed list of items in shopping cart
    print('Detail Barang dalam Keranjang Belanja:')
    headers = ['Barang', 'Jumlah']
    rows = []
    for grocery, quantity in shopping_cart.items():
        rows.append([grocery, quantity])
    print(tabulate(rows, headers=headers, tablefmt='grid'))

    # Payment process
    while True:
        payment = int(input('Masukkan jumlah uang pembayaran: '))
        if payment < total_payment:
            print('Uang Anda kurang. Mohon masukkan jumlah uang yang cukup.')
        else:
            break
    
    change = payment - total_payment
    print('Pembayaran berhasil.')
    print('Kembali:', change)


# Main function
def main():
    while True:
        display_menu()
        choice = input('Pilih menu (1-5): ')

        if choice == '1':
            display_grocery_list()
        elif choice == '2':
            add_grocery()
        elif choice == '3':
            remove_grocery()
        elif choice == '4':
            buy_grocery()
        elif choice == '5':
            print('Terima kasih telah menggunakan program ini.')
            break
        else:
            print('Pilihan tidak valid. Silakan pilih kembali.')

main()
