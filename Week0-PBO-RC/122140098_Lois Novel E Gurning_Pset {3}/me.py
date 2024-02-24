open ("me.txt", "w" )

with open('me.txt', 'w') as f:
    teks = [
        "Nama: Noppan\n", 
        "NIM: 122140098\n", 
        "Resolusi tahun ini: Jago ngoding\n"]
    f.writelines (teks)