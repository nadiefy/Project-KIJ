from cryptography.fernet import Fernet
import os

# Generate kunci enkripsi secara acak
def generate_key():
    return Fernet.generate_key()

# Enkripsi isi file menggunakan kunci yang diberikan
def encrypt_file(filename, key):
    cipher_suite = Fernet(key)  # Inisialisasi objek Fernet dengan kunci 
    with open(filename, 'rb') as file:
        plaintext = file.read()  # Baca data teks biasa dari file
    encrypted_data = cipher_suite.encrypt(plaintext)  # Enkripsi teks biasa
    with open(filename + '.enkripsi', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)  # Tulis data yang terenkripsi ke file baru

# Enkripsi gambar tanpa mengubah fungsi enkripsi teks
def encrypt_image(filename, key):
    cipher_suite = Fernet(key)  # Inisialisasi objek Fernet dengan kunci 
    with open(filename, 'rb') as file:
        image_data = file.read()  # Baca data gambar dari file
    encrypted_data = cipher_suite.encrypt(image_data)  # Enkripsi data gambar
    with open(filename + '.enkripsi', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)  # Tulis data yang terenkripsi ke file baru

# Dekripsi isi file terenkripsi menggunakan kunci yang diberikan
def decrypt_file(encrypted_filename, key):
    cipher_suite = Fernet(key)  # Inisialisasi objek Fernet dengan kunci
    with open(encrypted_filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()  # Baca data terenkripsi dari file
    decrypted_data = cipher_suite.decrypt(encrypted_data)  # Dekripsi data
    decrypted_filename = encrypted_filename.replace('.enkripsi', '_dekripsi')  # Generate nama file baru

    # Hapus ekstensi .dekripsi hanya untuk gambar
    if '.png' in decrypted_filename or '.jpg' in decrypted_filename:
        decrypted_filename = decrypted_filename.replace('.dekripsi', '')

    with open(decrypted_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)  # Tulis data yang sudah didekripsi ke file baru

# Hapus file dengan ekstensi .dekripsi
def delete_dekripsi_files():
    for filename in os.listdir():
        if filename.endswith('.dekripsi'):
            os.remove(filename)

key = generate_key()  # Hasilkan kunci enkripsi
source_text_file = 'plaintext.txt'  # Tentukan file sumber teks yang akan dienkripsi
source_image_file = 'manutd.png'  # Tentukan file sumber gambar yang akan dienkripsi

# Enkripsi file teks menggunakan kunci yang dihasilkan
encrypt_file(source_text_file, key)
print(f'{source_text_file} enkripsi.')  # Cetak pesan yang menunjukkan keberhasilan enkripsi

# Enkripsi file gambar menggunakan kunci yang dihasilkan
encrypt_image(source_image_file, key)
print(f'{source_image_file} enkripsi.')  # Cetak pesan yang menunjukkan keberhasilan enkripsi

# Dekripsi file terenkripsi teks menggunakan kunci yang sama
encrypted_text_file = source_text_file + '.enkripsi'
decrypt_file(encrypted_text_file, key)
print(f'{encrypted_text_file} dekripsi.')  # Cetak pesan yang menunjukkan keberhasilan dekripsi

# Dekripsi file terenkripsi gambar menggunakan kunci yang sama
encrypted_image_file = source_image_file + '.enkripsi'
decrypt_file(encrypted_image_file, key)
print(f'{encrypted_image_file} dekripsi.')  # Cetak pesan yang menunjukkan keberhasilan dekripsi

# Ubah nama gambar yang sudah di-dekripsi
delete_dekripsi_files()
