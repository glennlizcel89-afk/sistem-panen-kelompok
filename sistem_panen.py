
def input_data_panen():
    komoditas = input("Masukkan jenis komoditas: ") # Perubahan di branch fitur-input
    jumlah = float(input("Masukkan jumlah hasil panen (kilogram): ")) # Perubahan di branch fitur-input

    return {
        "komoditas": komoditas,
        "jumlah": jumlah
    }


if __name__ == "__main__":
    data = input_data_panen()

    print("\nData panen fitur-input:") # Perubahan di branch fitur-input
    print(f"Jenis Komoditas : {data['komoditas']}")
    print(f"Jumlah Panen    : {data['jumlah']} kilogram")
