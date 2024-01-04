from cryptography.fernet import Fernet

# Menghasilkan kunci enkripsi secara acak
def generate_key():
    return Fernet.generate_key()

# Enkripsi isi file menggunakan kunci yang diberikan
def encrypt_file(filename, key):
    cipher_suite = Fernet(key)  # Inisialisasi objek Fernet dengan kunci enkripsi
    with open(filename, 'rb') as file:
        plaintext = file.read()  # Baca data teks biasa dari file
    encrypted_data = cipher_suite.encrypt(plaintext)  # Enkripsi data teks biasa
    with open(filename + '.enkripsi', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)  # Tulis data yang terenkripsi ke file baru

# Enkripsi gambar tanpa mengubah fungsi enkripsi txt
def encrypt_image(filename, key):
    cipher_suite = Fernet(key)  # Inisialisasi objek Fernet dengan kunci enkripsi
    with open(filename, 'rb') as file:
        image_data = file.read()  # Baca data gambar dari file
    encrypted_data = cipher_suite.encrypt(image_data)  # Enkripsi data gambar
    with open(filename + '.enkripsi', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)  # Tulis data yang terenkripsi ke file baru

# Menghasilkan kunci enkripsi
key = generate_key()

# Tentukan file sumber yang akan dienkripsi (teks)
source_text_file = 'plaintext.txt'
# Enkripsi file teks menggunakan kunci yang dihasilkan
encrypt_file(source_text_file, key)
print(f'{source_text_file} enkripsi.')  # Cetak pesan yang menunjukkan keberhasilan enkripsi

# Tentukan file sumber yang akan dienkripsi (gambar)
source_image_file = 'manutd.png'
# Enkripsi file gambar menggunakan kunci yang dihasilkan
encrypt_image(source_image_file, key)
print(f'{source_image_file} enkripsi.')  # Cetak pesan yang menunjukkan keberhasilan enkripsi

# Cetak konten yang terenkripsi dalam format heksadesimal untuk file teks
encrypted_text_filename = source_text_file + '.enkripsi'
with open(encrypted_text_filename, 'rb') as encrypted_text_file:
    encrypted_text_data = encrypted_text_file.read()
    encrypted_text = encrypted_text_data.hex()
    print("Hasil Enkripsi (Teks):", encrypted_text)

# Cetak konten yang terenkripsi dalam format heksadesimal untuk file gambar
encrypted_image_filename = source_image_file + '.enkripsi'
with open(encrypted_image_filename, 'rb') as encrypted_image_file:
    encrypted_image_data = encrypted_image_file.read()
    encrypted_image = encrypted_image_data.hex()
    print("Hasil Enkripsi (Gambar):", encrypted_image)
