
# PDF Password Brute-Force Script

Script ini digunakan untuk melakukan brute-force pada file PDF yang terkunci menggunakan wordlist dengan bantuan tool **pdfcrack**.

## Fitur
- Memanfaatkan **pdfcrack** untuk mencoba menemukan password file PDF yang terkunci.
- Mendukung penggunaan wordlist (default: `rockyou.txt`).
- Memberikan hasil berupa password jika ditemukan.

## Prasyarat
Pastikan Anda telah menginstal:
1. Python (minimal versi 3.x)
2. **pdfcrack**  
   Untuk menginstal pdfcrack pada distribusi Linux berbasis Debian, gunakan:
   ```bash
   sudo apt install pdfcrack
   ```

## Cara Penggunaan
1. Clone repositori ini ke komputer Anda:
   ```bash
   git clone https://github.com/username/pdf-password-crack.git
   cd pdf-password-crack
   ```
2. Siapkan file PDF terkunci (`Target.pdf`) dan wordlist (`rockyou.txt`) di direktori yang sama dengan script Python.
3. Jalankan script:
   ```bash
   python3 pdf_bruteforce.py
   ```
4. Script akan mencoba menemukan password dari file PDF menggunakan wordlist.

## Output
- Jika password ditemukan:
  ```plaintext
  Password ditemukan!
  Password: [password_terdeteksi]
  ```
- Jika password tidak ditemukan:
  ```plaintext
  Password tidak ditemukan dalam wordlist. Coba wordlist lain.
  ```

## Catatan
- Pastikan file PDF dan wordlist tersedia di lokasi yang benar.
- Wordlist default adalah `rockyou.txt`, tetapi Anda dapat mengganti dengan wordlist lain sesuai kebutuhan.
- Pastikan **pdfcrack** sudah terinstal sebelum menjalankan script.

### Dikembangkan oleh: **[zfernm](https://www.linkedin.com/in/samuel-hamonangan-s-099604255/)**
