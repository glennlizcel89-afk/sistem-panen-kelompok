
def input_data_panen():
    komoditas = input("Masukkan nama komoditas panen: ") # Perubahan di branch main
    jumlah = float(input("Masukkan jumlah hasil panen (kg): "))

    return {
        "komoditas": komoditas,
        "jumlah": jumlah
    }


if __name__ == "__main__":
    data = input_data_panen()

    print("\nData hasil panen main:") # Perubahan di branch main
    print(f"Komoditas : {data['komoditas']}")
    print(f"Jumlah    : {data['jumlah']} kg")
