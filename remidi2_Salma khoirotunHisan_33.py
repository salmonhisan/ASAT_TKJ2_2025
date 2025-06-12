def luas_persegi(s):
    return s * s

def luas_lingkaran(r):
    return 3.14 * r * r

print("1. Luas Persegi\n2. Luas Lingkaran")
p = int(input("Pilihan Anda: "))

if p == 1:
    s = float(input("Masukkan sisi: "))
    print(f"Luas persegi dengan sisi {s} adalah {luas_persegi(s)}")
elif p == 2:
    r = float(input("Masukkan jari-jari: "))
    print(f"Luas lingkaran dengan jari-jari {r} adalah {luas_lingkaran(r):.2f}")
else:
    print("Pilihan tidak valid.")