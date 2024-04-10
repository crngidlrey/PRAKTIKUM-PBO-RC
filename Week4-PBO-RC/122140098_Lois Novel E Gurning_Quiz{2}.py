import random

kata_kunci = [
    'algoritma', 'biner', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'enkripsi', 'kerangka', 'fungsi', 'sampah', 'hash', 'indeks', 'iterator',
    'javascript', 'json', 'perpustakaan', 'loop', 'namespace', 'objek', 'operator',
    'overload', 'polimorfisme', 'antrian', 'rekursi', 'serialisasi', 'tumpukan',
    'template', 'variabel', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

langkah_hangman = ["""
    ------
    |    |
    |
    |
    |
    |
    |
------------""", """
    ------
    |    |
    |    O
    |
    |
    |
    |
------------""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
------------""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   /
    |
------------""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   / \\
    |
------------""", """
    ------
    |    |
    |    O
    |  --|
    |    |
    |   / \\
    |
------------""", """
    ------
    |    |
    |    O
    |  --|--
    |    |
    |   / \\
    |
------------"""]

def pilih_kata():
    return random.choice(kata_kunci)

def tampilkan_kata(kata, huruf_tertebak):
    tampilan = ''
    for huruf in kata:
        if huruf in huruf_tertebak:
            tampilan += huruf
        else:
            tampilan += '_'
    return tampilan

def hangman():
    kata = pilih_kata()
    huruf_tertebak = []
    percobaan = 6

    print("Selamat datang di Hangman!")
    print("Kata yang harus ditebak memiliki {} huruf.".format(len(kata)))

    while percobaan > 0:
        print("\nKata: ", tampilkan_kata(kata, huruf_tertebak))
        tebakan = input("Tebak satu huruf: ").lower()

        if len(tebakan) != 1 or not tebakan.isalpha():
            print("Silakan masukkan satu huruf saja.")
            continue

        if tebakan in huruf_tertebak:
            print("Anda sudah menebak huruf itu sebelumnya.")
            continue

        huruf_tertebak.append(tebakan)

        if tebakan not in kata:
            percobaan -= 1
            print("Tebakan salah! Anda memiliki {} percobaan lagi.".format(percobaan))
            print(langkah_hangman[6 - percobaan - 1])
        else:
            print("Tebakan benar!")

        if '_' not in tampilkan_kata(kata, huruf_tertebak):
            print("\nSelamat! Anda berhasil menebak kata:", kata)
            break

    if '_' in tampilkan_kata(kata, huruf_tertebak):
        print("\nMaaf, Anda gagal menebak kata tersebut. Kata yang benar adalah:", kata)

if __name__ == "__main__":
    hangman()