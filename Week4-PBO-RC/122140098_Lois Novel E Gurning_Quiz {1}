import random

def inisialisasi_papan():
    return [['?' for _ in range(3)] for _ in range(3)]

def tampilkan_papan(papan):
    for baris in papan:
        print(' '.join(baris))
    print()

def letakkan_bom(papan):
    baris = random.randint(0, 2)
    kolom = random.randint(0, 2)
    papan[baris][kolom] = 'X'

def gerakan_valid(baris, kolom):
    return 0 <= baris < 3 and 0 <= kolom < 3

def buka_kotak(papan, baris, kolom):
    if papan[baris][kolom] == 'X':
        return False
    else:
        return True

def cek_kemenangan(papan):
    for baris in papan:
        if '?' in baris:
            return False
    return True

def main():
    print("Selamat datang di Minesweeper!")
    while True:
        papan = inisialisasi_papan()
        letakkan_bom(papan)
        while True:
            tampilkan_papan(papan)
            baris = int(input("Masukkan baris (0-2): "))
            kolom = int(input("Masukkan kolom (0-2): "))

            if not gerakan_valid(baris, kolom):
                print("Gerakan tidak valid. Silakan masukkan baris dan kolom antara 0 dan 2.")
                continue

            if not buka_kotak(papan, baris, kolom):
                print("Game over! Anda memilih bom!")
                break
            else:
                if cek_kemenangan(papan):
                    tampilkan_papan(papan)
                    print("Selamat! Anda memenangkan permainan!")
                    break
                else:
                    print("Teruskan!")
        main_lagi = input("Apakah Anda ingin bermain lagi? (ya/tidak): ")
        if main_lagi.lower() != 'ya':
            print("Terima kasih telah bermain Minesweeper!")
            break

if __name__ == "__main__":
    main()
