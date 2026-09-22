
def input_data_panen():
    komoditas = input("Masukkan nama dan jenis komoditas panen: ") # Menggabungkan perubahan
    jumlah = float(input("Masukkan jumlah hasil panen (kg/kilogram): ")) # Menggabungkan perubahan

    return {
        "komoditas": komoditas,
        "jumlah": jumlah
    }


if __name__ == "__main__":
    data = input_data_panen()

    print("\nData hasil panen final:") # Menggabungkan perubahan
    print(f"Komoditas : {data['komoditas']}")
    print(f"Jumlah    : {data['jumlah']} kg")
