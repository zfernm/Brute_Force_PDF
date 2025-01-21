import subprocess

locked_pdf = "Chall.pdf"

wordlist = "rockyou.txt"  

command = ["pdfcrack", "-f", locked_pdf, "-w", wordlist]

try:
    print("Memulai brute-force menggunakan pdfcrack...")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if "found user-password" in result.stdout:
        print("\nPassword ditemukan!")
        for line in result.stdout.split("\n"):
            if "found user-password" in line:
                print(f"Password: {line.split()[-1]}")
                break
    else:
        print("\nPassword tidak ditemukan dalam wordlist. Coba wordlist lain.")
except FileNotFoundError:
    print("Error: pdfcrack tidak ditemukan. Install terlebih dahulu dengan 'sudo apt install pdfcrack'.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
