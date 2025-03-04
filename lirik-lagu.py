import sys
import time


def jalanin_lirik():
    lirik = [
        ("Dengar Laraku", 0.1),
        ("Suara hati ini memanggil namamu", 0.09),
        ("Karena separuh aku", 0.09),
        ("Menyentuh laramu", 0.09),
        ("Semua lukamu t'lah menjadi lirihku", 0.09),
        ("Kar'na separuh aku", 0.09),
        ("Dirimu", 0.09),
        ("-----", 0.1)
    ]

    delay = [0.3, 0.2, 0.3, 0.4, 0.6, 0.3, 0.3, 0.8]
    print("\n== Separuh Aku - Noah ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("// Code by DivzzOffc")


jalanin_lirik()
